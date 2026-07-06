"""Storage helpers — JSON file + optional Airtable."""

from __future__ import annotations

import json
import logging

from scholarship_grants.airtable_client import (
    airtable_enabled,
    clear_all_airtable,
    fetch_from_airtable,
    upsert_to_airtable,
)
from scholarship_grants.config import DATA_FILE
from scholarship_grants.models import Application

logger = logging.getLogger(__name__)
_last_airtable_error: str = ""


def storage_status() -> dict[str, str | bool | int]:
    return {
        "json_path": str(DATA_FILE),
        "airtable_enabled": airtable_enabled(),
        "last_airtable_error": _last_airtable_error,
        "json_count": _json_count(),
    }


def _json_count() -> int:
    try:
        _ensure_data_file()
        return len(json.loads(DATA_FILE.read_text(encoding="utf-8")))
    except Exception:
        return 0


def _ensure_data_file() -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")


def _load_from_json() -> list[Application]:
    _ensure_data_file()
    raw = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return [Application.from_dict(item) for item in raw]


def load_applications() -> list[Application]:
    """JSON is primary; merge Airtable records so synced data survives serverless cold starts."""
    json_apps = _load_from_json()
    if not airtable_enabled():
        return json_apps
    try:
        airtable_apps = fetch_from_airtable()
    except Exception as exc:
        logger.warning("Airtable read failed, using JSON only: %s", exc)
        return json_apps
    if not airtable_apps:
        return json_apps
    merged: dict[str, Application] = {a.id: a for a in airtable_apps if a.id}
    for app in json_apps:
        merged[app.id] = app
    return list(merged.values())


def clear_all_data() -> dict[str, str | bool | int]:
    """Wipe JSON storage and Airtable records."""
    global _last_airtable_error
    _ensure_data_file()
    DATA_FILE.write_text("[]", encoding="utf-8")
    deleted = 0
    airtable_cleared = False
    if airtable_enabled():
        try:
            deleted = clear_all_airtable()
            airtable_cleared = True
            _last_airtable_error = ""
        except Exception as exc:
            _last_airtable_error = str(exc)
            logger.warning("Airtable clear failed: %s", exc)
    return {
        "airtable_cleared": airtable_cleared,
        "airtable_deleted": deleted,
        "airtable_enabled": airtable_enabled(),
        "last_airtable_error": _last_airtable_error,
        "json_cleared": True,
    }


def save_applications(apps: list[Application]) -> None:
    _ensure_data_file()
    payload = [a.to_dict() for a in apps]
    DATA_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def sync_to_airtable(apps: list[Application] | None = None) -> dict[str, str | bool | int]:
    """Push current allocation data to Airtable (explicit demo export step)."""
    global _last_airtable_error
    records = apps if apps is not None else _load_from_json()
    airtable_synced = False
    if not records:
        _last_airtable_error = "No applications to sync"
        return {
            "airtable_synced": False,
            "airtable_enabled": airtable_enabled(),
            "count": 0,
        }
    if airtable_enabled():
        try:
            upsert_to_airtable(records)
            airtable_synced = True
            _last_airtable_error = ""
        except Exception as exc:
            _last_airtable_error = str(exc)
            logger.warning("Airtable sync failed: %s", exc)
    elif not airtable_enabled():
        _last_airtable_error = "AIRTABLE_API_KEY or AIRTABLE_BASE_ID not set on server"
    return {
        "airtable_synced": airtable_synced,
        "airtable_enabled": airtable_enabled(),
        "count": len(records),
    }


def append_applications(new_apps: list[Application]) -> tuple[list[Application], int]:
    """Append applications, skipping duplicates by email (case-insensitive)."""
    existing = _load_from_json()
    seen = {a.email.lower() for a in existing}
    added: list[Application] = []
    for app in new_apps:
        key = app.email.lower()
        if key in seen:
            continue
        added.append(app)
        seen.add(key)
    merged = existing + added
    save_applications(merged)
    return merged, len(added)


def add_application(app: Application) -> Application:
    apps = _load_from_json()
    apps.append(app)
    save_applications(apps)
    return app


def replace_all(apps: list[Application], *, sync_airtable: bool = True) -> dict[str, str | bool]:
    """Replace all applications. Returns sync metadata for API responses."""
    global _last_airtable_error
    _ensure_data_file()
    payload = [a.to_dict() for a in apps]
    DATA_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    airtable_synced = False
    if sync_airtable and airtable_enabled():
        try:
            upsert_to_airtable(apps)
            airtable_synced = True
            _last_airtable_error = ""
        except Exception as exc:
            _last_airtable_error = str(exc)
            logger.warning("Airtable sync failed: %s", exc)
    elif not airtable_enabled():
        _last_airtable_error = "AIRTABLE_API_KEY or AIRTABLE_BASE_ID not set on server"
    return {
        "airtable_synced": airtable_synced,
        "airtable_enabled": airtable_enabled(),
        "storage_path": str(DATA_FILE),
    }
