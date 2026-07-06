"""Online interview outcomes and waitlist promotion."""

from __future__ import annotations

from copy import deepcopy

from scholarship_grants.models import Application

INTERVIEW_OUTCOMES = {
    "": "— Pending —",
    "unattended": "Unattended",
    "attended_selected": "Attended — selected",
    "attended_rejected": "Attended — rejected",
}

REJECTION_REASONS = {
    "": "— Select reason —",
    "grades_mismatch": "Grades mismatch",
    "income_mismatch": "Income mismatch",
    "identity_mismatch": "Identity mismatch",
    "no_travel_budget": "Not having travel budget",
    "other": "Other (specify below)",
}

_SLOT_HELD = frozenset({"selected", "interview_confirmed"})
_SLOT_RELEASED = frozenset({"no_show", "interview_rejected"})


def format_rejection_reason(code: str, other_text: str = "") -> str:
    if not code:
        return ""
    if code == "other":
        return (other_text or "Other").strip()
    return REJECTION_REASONS.get(code, code)


def _promote_next_waitlist(apps: list[Application], freed_award: float) -> Application | None:
    waitlisted = sorted(
        (a for a in apps if a.status == "waitlist"),
        key=lambda a: a.applied_at,
    )
    if not waitlisted:
        return None
    promoted = waitlisted[0]
    for app in apps:
        if app.id == promoted.id:
            app.status = "selected"
            app.interview_outcome = ""
            app.rejection_reason = ""
            app.rejection_reason_code = ""
            app.notes = "Promoted from waitlist — interview slot opened (FIFO)"
            return app
    return None


def apply_interview_outcome(
    apps: list[Application],
    app_id: str,
    outcome: str,
    rejection_reason_code: str = "",
    rejection_other: str = "",
) -> tuple[list[Application], Application, Application | None]:
    """Record interview outcome; release slot and promote waitlist on no-show / rejection."""
    updated = [deepcopy(a) for a in apps]
    target: Application | None = None
    for app in updated:
        if app.id == app_id:
            target = app
            break
    if target is None:
        raise ValueError("Application not found")

    if outcome not in {"", "unattended", "attended_selected", "attended_rejected"}:
        raise ValueError("Invalid interview outcome")

    if outcome == "attended_rejected" and not rejection_reason_code:
        raise ValueError("Rejection reason is required")

    if outcome == "attended_rejected" and rejection_reason_code == "other" and not rejection_other.strip():
        raise ValueError("Please specify the rejection reason")

    if target.status not in _SLOT_HELD | _SLOT_RELEASED:
        if outcome:
            raise ValueError("Interview can only be recorded for students selected for interview")

    promoted: Application | None = None
    was_holding_slot = target.status == "selected"

    target.interview_outcome = outcome
    target.rejection_reason_code = rejection_reason_code if outcome == "attended_rejected" else ""
    target.rejection_reason = (
        format_rejection_reason(rejection_reason_code, rejection_other)
        if outcome == "attended_rejected"
        else ""
    )

    if outcome == "attended_selected":
        target.status = "interview_confirmed"
        target.notes = "Interview attended — scholarship confirmed"
    elif outcome == "unattended":
        target.status = "no_show"
        target.notes = "Did not attend online interview — slot released"
        if was_holding_slot:
            promoted = _promote_next_waitlist(updated, target.award_usd)
    elif outcome == "attended_rejected":
        target.status = "interview_rejected"
        target.notes = f"Interview rejected — {target.rejection_reason}"
        if was_holding_slot:
            promoted = _promote_next_waitlist(updated, target.award_usd)
    elif outcome == "":
        if target.status in _SLOT_RELEASED:
            target.status = "selected"
        target.rejection_reason = ""
        target.rejection_reason_code = ""
        target.notes = ""

    return updated, target, promoted


def interview_summary(apps: list[Application]) -> dict[str, int]:
    return {
        "interview_confirmed": sum(1 for a in apps if a.interview_outcome == "attended_selected"),
        "no_show": sum(1 for a in apps if a.interview_outcome == "unattended"),
        "interview_rejected": sum(1 for a in apps if a.interview_outcome == "attended_rejected"),
        "interview_pending": sum(
            1 for a in apps if a.status in _SLOT_HELD and not a.interview_outcome
        ),
    }
