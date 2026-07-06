"""JSON file storage with optional Airtable sync."""

from __future__ import annotations

import json
from typing import Any

from scholarship_grants.airtable_client import (
    airtable_enabled,
    fetch_from_airtable,
    upsert_to_airtable,
)
from scholarship_grants.config import DATA_FILE
from scholarship_grants.models import Application


def _ensure_data_file() -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")


def load_applications() -> list[Application]:
    if airtable_enabled():
        try:
            return fetch_from_airtable()
        except Exception:
            pass
    _ensure_data_file()
    raw = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return [Application.from_dict(item) for item in raw]


def save_applications(apps: list[Application]) -> None:
    _ensure_data_file()
    payload = [a.to_dict() for a in apps]
    DATA_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    if airtable_enabled():
        try:
            upsert_to_airtable(apps)
        except Exception:
            pass


def add_application(app: Application) -> Application:
    apps = load_applications()
    apps.append(app)
    save_applications(apps)
    return app


def replace_all(apps: list[Application]) -> None:
    save_applications(apps)
