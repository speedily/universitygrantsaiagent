"""Tests for interview outcomes and waitlist promotion."""

from scholarship_grants.interview import apply_interview_outcome
from scholarship_grants.models import Application


def _selected(name: str, applied_at: str, award: float = 150000) -> Application:
    return Application(
        name=name,
        email=f"{name.lower().replace(' ', '')}@u.edu",
        country="India",
        semester="Fall 2026",
        marks_pct=80,
        family_income_local=800000,
        currency_code="INR",
        applied_at=applied_at,
        status="selected",
        tier="A",
        award_usd=award,
    )


def _waitlist(name: str, applied_at: str) -> Application:
    return Application(
        name=name,
        email=f"{name.lower().replace(' ', '')}@u.edu",
        country="India",
        semester="Fall 2026",
        marks_pct=75,
        family_income_local=700000,
        currency_code="INR",
        applied_at=applied_at,
        status="waitlist",
        tier="A",
        award_usd=150000,
    )


def test_unattended_promotes_waitlist():
    apps = [
        _selected("Alice", "2026-07-01T08:00:00+00:00"),
        _waitlist("Bob", "2026-07-01T09:00:00+00:00"),
    ]
    updated, target, promoted = apply_interview_outcome(apps, apps[0].id, "unattended")
    assert target.status == "no_show"
    assert target.interview_outcome == "unattended"
    assert promoted is not None
    assert promoted.name == "Bob"
    assert promoted.status == "selected"


def test_attended_rejected_requires_reason():
    apps = [_selected("Alice", "2026-07-01T08:00:00+00:00")]
    try:
        apply_interview_outcome(apps, apps[0].id, "attended_rejected")
        assert False, "should raise"
    except ValueError as exc:
        assert "reason" in str(exc).lower()


def test_attended_rejected_with_reason():
    apps = [
        _selected("Alice", "2026-07-01T08:00:00+00:00"),
        _waitlist("Bob", "2026-07-01T09:00:00+00:00"),
    ]
    updated, target, promoted = apply_interview_outcome(
        apps, apps[0].id, "attended_rejected", "grades_mismatch"
    )
    assert target.status == "interview_rejected"
    assert target.rejection_reason == "Grades mismatch"
    assert promoted.name == "Bob"


def test_attended_rejected_other_reason():
    apps = [_selected("Alice", "2026-07-01T08:00:00+00:00")]
    updated, target, _ = apply_interview_outcome(
        apps, apps[0].id, "attended_rejected", "other", "Could not verify documents"
    )
    assert target.status == "interview_rejected"
    assert target.rejection_reason_code == "other"
    assert target.rejection_reason == "Could not verify documents"


def test_attended_selected_confirms():
    apps = [_selected("Alice", "2026-07-01T08:00:00+00:00")]
    updated, target, promoted = apply_interview_outcome(apps, apps[0].id, "attended_selected")
    assert target.status == "interview_confirmed"
    assert promoted is None
