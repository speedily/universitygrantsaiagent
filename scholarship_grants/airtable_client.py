"""Airtable REST client — MCP-style external tool integration."""

from __future__ import annotations

from typing import Any
from urllib.parse import quote

import httpx

from scholarship_grants.config import (
    AIRTABLE_API_KEY,
    AIRTABLE_BASE_ID,
    AIRTABLE_TABLE,
)
from scholarship_grants.models import Application

TIMEOUT = 20.0


def airtable_enabled() -> bool:
    return bool(AIRTABLE_API_KEY and AIRTABLE_BASE_ID)


def _headers() -> dict[str, str]:
    return {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json",
    }


def _table_url() -> str:
    return f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{quote(AIRTABLE_TABLE)}"


def _fields(app: Application) -> dict[str, Any]:
    return {
        "Application ID": app.id,
        "Name": app.name,
        "Email": app.email,
        "Country": app.country,
        "Semester": app.semester,
        "Academic Year": app.academic_year,
        "Marks Pct": app.marks_pct,
        "Grade": app.grade,
        "Family Income Local": app.family_income_local,
        "Currency": app.currency_code,
        "Family Income USD": app.family_income_usd,
        "Applied At": app.applied_at,
        "Status": app.status,
        "Tier": app.tier,
        "Award USD": app.award_usd,
        "Interview Outcome": app.interview_outcome,
        "Rejection Reason": app.rejection_reason,
        "Notes": app.notes,
    }


def _from_record(record: dict[str, Any]) -> Application:
    f = record.get("fields", {})
    legacy_inr = float(f.get("Family Income INR") or 0)
    local = float(f.get("Family Income Local") or legacy_inr or 0)
    currency = str(f.get("Currency") or ("INR" if legacy_inr else "USD"))
    return Application(
        id=str(f.get("Application ID") or record.get("id", "")),
        name=str(f.get("Name", "")),
        email=str(f.get("Email", "")),
        country=str(f.get("Country", "")),
        semester=str(f.get("Semester", "")),
        academic_year=str(f.get("Academic Year", "2026–2027")),
        marks_pct=float(f.get("Marks Pct") or 0),
        grade=str(f.get("Grade") or ""),
        family_income_local=local,
        currency_code=currency,
        family_income_usd=float(f.get("Family Income USD") or 0),
        interview_outcome=str(f.get("Interview Outcome") or ""),
        rejection_reason=str(f.get("Rejection Reason") or ""),
        applied_at=str(f.get("Applied At") or ""),
        status=str(f.get("Status") or "pending"),
        tier=str(f.get("Tier") or ""),
        award_usd=float(f.get("Award USD") or 0),
        notes=str(f.get("Notes") or ""),
    )


def fetch_from_airtable() -> list[Application]:
    if not airtable_enabled():
        return []
    apps: list[Application] = []
    offset: str | None = None
    with httpx.Client(timeout=TIMEOUT) as client:
        while True:
            params: dict[str, str] = {}
            if offset:
                params["offset"] = offset
            resp = client.get(_table_url(), headers=_headers(), params=params)
            resp.raise_for_status()
            data = resp.json()
            for rec in data.get("records", []):
                apps.append(_from_record(rec))
            offset = data.get("offset")
            if not offset:
                break
    return apps


def upsert_to_airtable(apps: list[Application]) -> None:
    if not airtable_enabled():
        return
    with httpx.Client(timeout=TIMEOUT) as client:
        for app in apps:
            payload = {"fields": _fields(app)}
            client.post(_table_url(), headers=_headers(), json=payload).raise_for_status()
