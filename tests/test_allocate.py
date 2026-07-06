"""Tests for deterministic allocation — capstone eval concept."""

from scholarship_grants.allocate import allocate_applications, is_eligible
from scholarship_grants.models import Application


def _app(**kwargs) -> Application:
    defaults = {
        "name": "Test",
        "email": "t@u.edu",
        "country": "India",
        "semester": "Fall 2026",
        "marks_pct": 75,
        "family_income_local": 800000,
        "currency_code": "INR",
        "applied_at": "2026-07-01T10:00:00+00:00",
    }
    defaults.update(kwargs)
    return Application(**defaults)


def test_eligible_high_income_rejected():
    assert not is_eligible(_app(family_income_local=15000, currency_code="USD"))


def test_eligible_low_marks_rejected():
    assert not is_eligible(_app(marks_pct=45))
    assert not is_eligible(_app(marks_pct=39))


def test_income_usd_conversion_eligible():
    app = _app(family_income_local=900000, currency_code="INR")
    assert app.family_income_usd == 10800.0
    assert is_eligible(app)


def test_tier_a_award():
    apps, summary = allocate_applications([_app(marks_pct=80)])
    assert apps[0].status == "selected"
    assert apps[0].tier == "A"
    assert apps[0].award_usd == 150000


def test_tier_b_award():
    apps, _ = allocate_applications([_app(marks_pct=55)])
    assert apps[0].tier == "B"
    assert apps[0].award_usd == 50000


def test_fifo_waitlist_when_budget_exceeded():
    batch = [
        _app(name="Early A", marks_pct=80, applied_at="2026-07-01T08:00:00+00:00"),
        _app(name="Late A", marks_pct=82, applied_at="2026-07-01T12:00:00+00:00"),
        _app(name="Third A", marks_pct=90, applied_at="2026-07-01T14:00:00+00:00"),
        _app(name="Fourth A", marks_pct=88, applied_at="2026-07-01T16:00:00+00:00"),
        _app(name="Fifth A", marks_pct=91, applied_at="2026-07-01T18:00:00+00:00"),
        _app(name="Sixth A", marks_pct=85, applied_at="2026-07-01T20:00:00+00:00"),
        _app(name="Seventh A", marks_pct=86, applied_at="2026-07-01T22:00:00+00:00"),
    ]
    apps, summary = allocate_applications(batch, budget_usd=1000000)
    selected = [a for a in apps if a.status == "selected"]
    waitlist = [a for a in apps if a.status == "waitlist"]
    assert len(selected) == 6
    assert len(waitlist) >= 1
    assert waitlist[0].name == "Seventh A"
    assert summary["spent_usd"] <= 1000000
