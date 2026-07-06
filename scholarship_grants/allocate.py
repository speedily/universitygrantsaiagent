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
from scholarship_grants.grading import grade_from_marks
from scholarship_grants.models import Application


def is_eligible(app: Application) -> bool:
    marks = float(app.marks_pct)
    grade = grade_from_marks(marks)
    marks_ok = marks >= MIN_MARKS_ELIGIBLE and grade != "FAIL"
    income_ok = app.family_income_usd < MAX_INCOME_USD
    return marks_ok and income_ok


def assign_tier(app: Application) -> tuple[str, float]:
    marks = float(app.marks_pct)
    if marks >= MIN_MARKS_TIER_A:
        return "A", TIER_A_AWARD_USD
    return "B", TIER_B_AWARD_USD


def allocate_applications(
    applications: list[Application],
    budget_usd: float = BUDGET_USD,
) -> tuple[list[Application], dict[str, float | int]]:
    """Return updated applications and summary stats."""
    apps = [deepcopy(a) for a in applications]
    for app in apps:
        app.grade = grade_from_marks(app.marks_pct)
        if not is_eligible(app):
            app.status = "ineligible"
            app.tier = ""
            app.award_usd = 0.0
            grade = app.grade
            if grade == "FAIL" or app.marks_pct < MIN_MARKS_ELIGIBLE:
                app.notes = "Does not meet admission (marks ≥40%) or scholarship marks (≥50%)"
            else:
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
