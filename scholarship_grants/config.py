"""Configuration from environment."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

_default_data = ROOT / "data" / "applications.json"
if os.getenv("VERCEL"):
    DATA_FILE = Path("/tmp/applications.json")
else:
    DATA_FILE = Path(os.getenv("STORAGE_PATH", str(_default_data)))

BUDGET_USD = float(os.getenv("SCHOLARSHIP_BUDGET_USD", "1000000"))
TIER_A_AWARD_USD = float(os.getenv("TIER_A_AWARD_USD", "150000"))
TIER_B_AWARD_USD = float(os.getenv("TIER_B_AWARD_USD", "50000"))
MAX_INCOME_USD = float(os.getenv("MAX_INCOME_USD", "12000"))
MIN_MARKS_ELIGIBLE = float(os.getenv("MIN_MARKS_ELIGIBLE", "50"))
MIN_MARKS_TIER_A = float(os.getenv("MIN_MARKS_TIER_A", "70"))

APPLICATION_DEADLINE = os.getenv("APPLICATION_DEADLINE", "2026-08-15")
CURRENT_SEMESTER = os.getenv("CURRENT_SEMESTER", "Fall 2026")
ACADEMIC_YEAR = os.getenv("ACADEMIC_YEAR", "2026–2027")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "openai/gpt-4o-mini")

AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY", "")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID", "")
AIRTABLE_TABLE = os.getenv("AIRTABLE_APPLICATIONS_TABLE", "Student Applications")
