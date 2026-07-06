"""Data models for scholarship applications."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from scholarship_grants.currency import currency_for_country, to_usd
from scholarship_grants.grading import grade_from_marks


def server_now_iso() -> str:
    """ISO timestamp when the form was received (server local timezone)."""
    return datetime.now().astimezone().isoformat()


def format_applied_at(iso: str) -> tuple[str, str]:
    """Return (date, time) in the server's local timezone."""
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        local = dt.astimezone()
        return local.strftime("%Y-%m-%d"), local.strftime("%H:%M:%S")
    except (TypeError, ValueError):
        raw = (iso or "")[:19]
        parts = raw.split("T")
        return parts[0] if parts else "—", parts[1] if len(parts) > 1 else "—"


def server_timezone_label() -> str:
    local = datetime.now().astimezone()
    name = local.tzname()
    return name if name else "server local"


def applied_at_sort_key(iso: str) -> str:
    return iso or ""


@dataclass
class Application:
    name: str
    email: str
    country: str
    semester: str
    marks_pct: float
    family_income_local: float
    currency_code: str = "USD"
    family_income_usd: float = 0.0
    academic_year: str = "2026–2027"
    phone: str = ""
    grade: str = ""
    id: str = field(default_factory=lambda: str(uuid4()))
    applied_at: str = field(default_factory=server_now_iso)
    status: str = "pending"
    tier: str = ""
    award_usd: float = 0.0
    notes: str = ""
    interview_outcome: str = ""
    rejection_reason_code: str = ""
    rejection_reason: str = ""

    def __post_init__(self) -> None:
        if not self.currency_code:
            self.currency_code = currency_for_country(self.country)
        if self.family_income_usd <= 0 and self.family_income_local > 0:
            self.family_income_usd = to_usd(self.family_income_local, self.currency_code)
        self.grade = grade_from_marks(self.marks_pct)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        applied_date, applied_time = format_applied_at(self.applied_at)
        data["applied_date"] = applied_date
        data["applied_time"] = applied_time
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Application:
        data = dict(data)
        if "family_income_inr" in data and "family_income_local" not in data:
            data["family_income_local"] = data.pop("family_income_inr")
            data.setdefault("currency_code", "INR")
        known = {f.name for f in cls.__dataclass_fields__.values()}  # type: ignore[attr-defined]
        return cls(**{k: v for k, v in data.items() if k in known})
