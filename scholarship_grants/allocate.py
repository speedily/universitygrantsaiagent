"""Deterministic, bias-free scholarship allocation engine."""

from __future__ import annotations

from copy import deepcopy

from scholarship_grants.config import (
    BUDGET_USD,
    MAX_INCOME_USD,
    MIN_MARKS_ELIGIBLE,
    MIN_MARKS_TIER_A,
    TIER_A_AWARD_USD,
    TIER_B_AWARD_USD,
)
from scholarship_grants.models import Application


def normalize_grade(grade: str) -> str:
    return (grade or "").strip().upper()


def effective_marks_pct(app: Application) -> float:
    grade = normalize_grade(app.grade)
    if grade == "A":
        return max(app.marks_pct, 85.0)
    if grade == "B":
        return max(app.marks_pct, 60.0)
    if grade == "C":
        return max(app.marks_pct, 45.0)
    return float(app.marks_pct)


def is_eligible(app: Application) -> bool:
    marks = effective_marks_pct(app)
    grade = normalize_grade(app.grade)
    marks_ok = marks >= MIN_MARKS_ELIGIBLE or grade in {"A", "B"}
    income_ok = app.family_income_usd < MAX_INCOME_USD
    return marks_ok and income_ok


def assign_tier(app: Application) -> tuple[str, float]:
    marks = effective_marks_pct(app)
    grade = normalize_grade(app.grade)
    if marks >= MIN_MARKS_TIER_A or grade == "A":
        return "A", TIER_A_AWARD_USD
    return "B", TIER_B_AWARD_USD


def allocate_applications(
    applications: list[Application],
    budget_usd: float = BUDGET_USD,
) -> tuple[list[Application], dict[str, float | int]]:
    """Return updated applications and summary stats."""
    apps = [deepcopy(a) for a in applications]
    for app in apps:
        if not is_eligible(app):
            app.status = "ineligible"
            app.tier = ""
            app.award_usd = 0.0
            app.notes = "Does not meet income (< $12,000 USD equivalent) or marks eligibility"
            continue
        tier, award = assign_tier(app)
        app.tier = tier
        app.award_usd = award
        app.status = "eligible"
        app.notes = ""

    eligible = [a for a in apps if a.status == "eligible"]
    eligible.sort(key=lambda a: a.applied_at)

    spent = 0.0
    for app in eligible:
        if spent + app.award_usd <= budget_usd:
            app.status = "selected"
            app.notes = "Selected — fair rules + FIFO timestamp"
            spent += app.award_usd
        else:
            app.status = "waitlist"
            app.notes = "Waitlist — budget cap reached; FIFO order preserved"

    summary = {
        "budget_usd": budget_usd,
        "spent_usd": spent,
        "remaining_usd": budget_usd - spent,
        "selected_count": sum(1 for a in apps if a.status == "selected"),
        "waitlist_count": sum(1 for a in apps if a.status == "waitlist"),
        "ineligible_count": sum(1 for a in apps if a.status == "ineligible"),
        "total_applications": len(apps),
    }
    return apps, summary
