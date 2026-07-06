"""Airtable REST client — MCP-style external tool integration."""

from __future__ import annotations

import logging
import re
from typing import Any
from urllib.parse import quote

import httpx

from scholarship_grants.airtable_schema import (
    AIRTABLE_COLUMNS,
    AIRTABLE_SELECT_FIELDS,
    application_to_airtable_fields,
    airtable_record_to_application,
)
from scholarship_grants.config import (
    AIRTABLE_API_KEY,
    AIRTABLE_BASE_ID,
    AIRTABLE_TABLE,
)

TIMEOUT = 20.0
logger = logging.getLogger(__name__)
_UNKNOWN_FIELD_RE = re.compile(r'Unknown field name: "([^"]+)"')
_INVALID_SELECT_RE = re.compile(r'select option ""([^"]*)""')
_skipped_columns: set[str] = set()


def airtable_enabled() -> bool:
    return bool(AIRTABLE_API_KEY and AIRTABLE_BASE_ID)


def _headers() -> dict[str, str]:
    return {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}",
        "Content-Type": "application/json",
    }


def _table_url() -> str:
    return f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{quote(AIRTABLE_TABLE)}"


def expected_airtable_columns() -> list[str]:
    return [name for name, _ in AIRTABLE_COLUMNS]


def _write_record(client: httpx.Client, method: str, url: str, fields: dict[str, Any]) -> httpx.Response:
    """POST/PATCH dropping unknown columns or invalid select values until Airtable accepts."""
    global _skipped_columns
    payload_fields = {k: v for k, v in fields.items() if k not in _skipped_columns}
    for _ in range(12):
        resp = client.request(method, url, headers=_headers(), json={"fields": payload_fields})
        if resp.status_code != 422:
            return resp
        body = resp.json()
        err = body.get("error", {})
        err_type = err.get("type", "")
        message = err.get("message", "")

        if err_type == "UNKNOWN_FIELD_NAME":
            match = _UNKNOWN_FIELD_RE.search(message)
            if not match:
                return resp
            bad = match.group(1)
            if bad in _skipped_columns or bad not in payload_fields:
                return resp
            _skipped_columns.add(bad)
            logger.warning("Airtable column not in base (skipped for session): %s", bad)
            del payload_fields[bad]
            continue

        if err_type == "INVALID_MULTIPLE_CHOICE_OPTIONS":
            match = _INVALID_SELECT_RE.search(message)
            invalid_val = match.group(1) if match else None
            removed_key = None
            for key in list(payload_fields.keys()):
                if key not in AIRTABLE_SELECT_FIELDS:
                    continue
                if invalid_val is None or str(payload_fields[key]) == invalid_val:
                    removed_key = key
                    break
            if not removed_key:
                return resp
            logger.warning(
                "Airtable rejected select value for %s (%r) — omitted; value kept in long-text fields",
                removed_key,
                payload_fields.pop(removed_key),
            )
            continue

        return resp
    return resp


def _list_records() -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    offset: str | None = None
    with httpx.Client(timeout=TIMEOUT) as client:
        while True:
            params: dict[str, str] = {}
            if offset:
                params["offset"] = offset
            resp = client.get(_table_url(), headers=_headers(), params=params)
            resp.raise_for_status()
            data = resp.json()
            records.extend(data.get("records", []))
            offset = data.get("offset")
            if not offset:
                break
    return records


def upsert_to_airtable(apps: list) -> None:
    if not airtable_enabled():
        return
    global _skipped_columns
    _skipped_columns = set()
    existing: dict[str, str] = {}
    for rec in _list_records():
        app_id = str(rec.get("fields", {}).get("Application ID") or "")
        if app_id:
            existing[app_id] = rec["id"]

    with httpx.Client(timeout=TIMEOUT) as client:
        for app in apps:
            fields = application_to_airtable_fields(app)
            record_id = existing.get(app.id)
            if record_id:
                resp = _write_record(client, "PATCH", f"{_table_url()}/{record_id}", fields)
            else:
                resp = _write_record(client, "POST", _table_url(), fields)
            try:
                resp.raise_for_status()
            except httpx.HTTPStatusError as exc:
                body = exc.response.text[:400] if exc.response is not None else ""
                raise RuntimeError(f"Airtable HTTP {exc.response.status_code}: {body}") from exc
            if not record_id and resp.json().get("id"):
                existing[app.id] = resp.json()["id"]
    if _skipped_columns:
        logger.warning(
            "Add these columns in Airtable for full dashboard sync: %s",
            sorted(_skipped_columns),
        )


def fetch_from_airtable() -> list:
    if not airtable_enabled():
        return []
    return [airtable_record_to_application(rec) for rec in _list_records()]


def clear_all_airtable() -> int:
    """Delete every record in the table. Returns count deleted."""
    if not airtable_enabled():
        return 0
    deleted = 0
    with httpx.Client(timeout=TIMEOUT) as client:
        while True:
            resp = client.get(
                _table_url(),
                headers=_headers(),
                params={"pageSize": "10"},
            )
            resp.raise_for_status()
            records = resp.json().get("records", [])
            if not records:
                break
            ids = [r["id"] for r in records]
            del_resp = client.delete(
                _table_url(),
                headers=_headers(),
                params=[("records[]", rid) for rid in ids],
            )
            del_resp.raise_for_status()
            deleted += len(ids)
    return deleted
