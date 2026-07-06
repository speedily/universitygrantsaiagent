"""Airtable column definitions — must match dashboard + application form."""

from __future__ import annotations

from typing import Any

from scholarship_grants.interview import INTERVIEW_OUTCOMES, REJECTION_REASONS
from scholarship_grants.models import Application, format_applied_at

# Single-select columns — omit when empty (Airtable rejects blank options).
AIRTABLE_SELECT_FIELDS = frozenset({
    "Grade",
    "Status",
    "Tier",
    "Interview Outcome",
    "Rejection Reason Code",
})

# Back-compat alias used in field filter below.
SELECT_FIELDS = AIRTABLE_SELECT_FIELDS

# All columns to create in Airtable (see data/airtable-omni-prompt.md).
AIRTABLE_COLUMNS = [
    ("Application ID", "Single line text"),
    ("Name", "Single line text"),
    ("Email", "Email"),
    ("Phone", "Single line text"),
    ("Country", "Single line text"),
    ("Semester", "Single line text"),
    ("Academic Year", "Single line text"),
    ("Marks Pct", "Number"),
    ("Grade", "Single select"),
    ("Income Local", "Number"),
    ("Currency", "Single line text"),
    ("Income USD", "Number"),
    ("Applied At", "Single line text"),
    ("Applied Date", "Single line text"),
    ("Applied Time", "Single line text"),
    ("Status", "Single select"),
    ("Tier", "Single select"),
    ("Award USD", "Number"),
    ("Interview Outcome", "Single select"),
    ("Interview", "Single line text"),
    ("Rejection Reason Code", "Single select"),
    ("Rejection Reason", "Long text"),
    ("Notes", "Long text"),
]


def _interview_label(code: str) -> str:
    return INTERVIEW_OUTCOMES.get(code, code) if code else ""


def _rejection_label(code: str) -> str:
    return REJECTION_REASONS.get(code, code) if code else ""


def application_to_airtable_fields(app: Application) -> dict[str, Any]:
    """Map application to Airtable field names (full dashboard parity)."""
    applied_date, applied_time = format_applied_at(app.applied_at)
    grade = app.grade if app.grade in {"A", "B", "C"} else ""
    rejection_reason = app.rejection_reason.strip()
    if not rejection_reason and app.rejection_reason_code:
        rejection_reason = _rejection_label(app.rejection_reason_code)
    elif app.rejection_reason_code == "other" and rejection_reason:
        rejection_reason = f"Other: {rejection_reason}"
    raw: dict[str, Any] = {
        "Application ID": app.id,
        "Name": app.name,
        "Email": app.email,
        "Phone": app.phone,
        "Country": app.country,
        "Semester": app.semester,
        "Academic Year": app.academic_year,
        "Marks Pct": app.marks_pct,
        "Grade": grade,
        "Income Local": app.family_income_local,
        "Currency": app.currency_code,
        "Income USD": app.family_income_usd,
        "Applied At": app.applied_at,
        "Applied Date": applied_date,
        "Applied Time": applied_time,
        "Status": app.status,
        "Tier": app.tier,
        "Award USD": app.award_usd,
        "Interview Outcome": app.interview_outcome,
        "Interview": _interview_label(app.interview_outcome),
        "Rejection Reason Code": app.rejection_reason_code,
        "Rejection Reason": rejection_reason,
        "Notes": app.notes,
    }
    return {
        key: value
        for key, value in raw.items()
        if value is not None and not (key in SELECT_FIELDS and value == "")
    }


def airtable_record_to_application(record: dict[str, Any]) -> Application:
    f = record.get("fields", {})
    legacy_inr = float(f.get("Family Income INR") or 0)
    local = float(f.get("Income Local") or f.get("Family Income Local") or legacy_inr or 0)
    currency = str(f.get("Currency") or ("INR" if legacy_inr else "USD"))
    applied_at = str(f.get("Applied At") or "")
    if not applied_at and f.get("Applied Date"):
        applied_at = f"{f.get('Applied Date')}T{f.get('Applied Time', '00:00:00')}"
    return Application(
        id=str(f.get("Application ID") or record.get("id", "")),
        name=str(f.get("Name", "")),
        email=str(f.get("Email", "")),
        phone=str(f.get("Phone") or ""),
        country=str(f.get("Country", "")),
        semester=str(f.get("Semester", "")),
        academic_year=str(f.get("Academic Year", "2026–2027")),
        marks_pct=float(f.get("Marks Pct") or 0),
        grade=str(f.get("Grade") or ""),
        family_income_local=local,
        currency_code=currency,
        family_income_usd=float(f.get("Income USD") or f.get("Family Income USD") or 0),
        applied_at=applied_at,
        status=str(f.get("Status") or "pending"),
        tier=str(f.get("Tier") or ""),
        award_usd=float(f.get("Award USD") or 0),
        interview_outcome=str(f.get("Interview Outcome") or ""),
        rejection_reason_code=str(f.get("Rejection Reason Code") or ""),
        rejection_reason=str(f.get("Rejection Reason") or ""),
        notes=str(f.get("Notes") or ""),
    )
