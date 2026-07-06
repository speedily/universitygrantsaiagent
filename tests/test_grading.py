"""Tests for marks → grade rules."""

from scholarship_grants.grading import grade_from_marks, is_admitted


def test_grade_a():
    assert grade_from_marks(70) == "A"
    assert grade_from_marks(88) == "A"


def test_grade_b():
    assert grade_from_marks(69) == "B"
    assert grade_from_marks(50) == "B"


def test_grade_c():
    assert grade_from_marks(49) == "C"
    assert grade_from_marks(40) == "C"


def test_grade_fail():
    assert grade_from_marks(39) == "FAIL"
    assert not is_admitted(39)
    assert is_admitted(40)
