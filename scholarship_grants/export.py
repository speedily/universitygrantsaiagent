"""CSV export for screening / final student lists."""

from __future__ import annotations

import csv
import io
from typing import Iterable

from scholarship_grants.models import Application

CSV_COLUMNS = [
    "name",
    "email",
    "country",
    "applied_date",
    "applied_time",
    "marks_pct",
    "grade",
    "family_income_local",
    "currency_code",
    "family_income_usd",
    "tier",
    "award_usd",
    "status",
    "interview_outcome",
    "rejection_reason",
    "notes",
]


def _row(app: Application) -> dict[str, str | float]:
    d = app.to_dict()
    return {col: d.get(col, "") for col in CSV_COLUMNS}


def applications_to_csv(apps: Iterable[Application], list_type: str = "all") -> str:
    """Build CSV string. list_type: all | screening | final."""
    items = list(apps)
    if list_type == "screening":
        items = [a for a in items if a.status in {"selected", "interview_confirmed", "waitlist"}]
    elif list_type == "final":
        items = [a for a in items if a.status == "interview_confirmed"]
    items.sort(key=lambda a: a.applied_at)

    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=CSV_COLUMNS, extrasaction="ignore")
    writer.writeheader()
    for app in items:
        writer.writerow(_row(app))
    return buf.getvalue()
