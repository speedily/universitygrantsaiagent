"""Letter grades derived from marks — admission and scholarship rules."""

from __future__ import annotations


def grade_from_marks(marks_pct: float) -> str:
    """A ≥70%, B 50–69%, C 40–49%, Fail <40%."""
    marks = float(marks_pct)
    if marks >= 70:
        return "A"
    if marks >= 50:
        return "B"
    if marks >= 40:
        return "C"
    return "FAIL"


def is_admitted(marks_pct: float) -> bool:
    """Applications below 40% are not accepted for admission."""
    return float(marks_pct) >= 40


def grade_scale_note() -> str:
    return (
        "Grade from marks: A (≥70%), B (50–69%), C (40–49%). "
        "Below 40% is Fail — not accepted. Scholarship requires marks ≥50%."
    )
