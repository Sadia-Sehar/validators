"""Module 3 (between.py): function between."""
import pytest
import validators

pytestmark = pytest.mark.member_a


@pytest.mark.smoke
@pytest.mark.ecp
def test_between_value_inside_range():
    assert validators.between(5, min_val=1, max_val=10) is True


@pytest.mark.bva
@pytest.mark.parametrize("value,expected", [
    (0, False), (1, True), (2, True), (9, True), (10, True), (11, False),
])
def test_between_integer_boundaries(value, expected):
    assert bool(validators.between(value, min_val=1, max_val=10)) is expected


@pytest.mark.bva
def test_between_equal_min_and_max_matching_value():
    assert validators.between(5, min_val=5, max_val=5) is True


@pytest.mark.bva
def test_between_equal_min_and_max_other_value():
    assert not validators.between(6, min_val=5, max_val=5)


@pytest.mark.negative
def test_between_min_greater_than_max_is_invalid():
    assert not validators.between(5, min_val=10, max_val=1)


@pytest.mark.ecp
def test_between_only_min_given():
    assert validators.between(5, min_val=1) is True


@pytest.mark.ecp
def test_between_only_max_given_fail():
    assert not validators.between(5, max_val=3)


def test_between_no_limits_always_valid():
    assert validators.between(5) is True


@pytest.mark.ecp
@pytest.mark.parametrize("value,expected", [(-5, True), (-11, False), (-1, True), (0, False)])
def test_between_negative_ranges(value, expected):
    assert bool(validators.between(value, min_val=-10, max_val=-1)) is expected


@pytest.mark.ecp
@pytest.mark.parametrize("value,expected", [(1.5, True), (0.99, False), (2.5, True), (2.51, False)])
def test_between_floats(value, expected):
    assert bool(validators.between(value, min_val=1.0, max_val=2.5)) is expected


def test_between_strings_compared_alphabetically():
    assert validators.between("b", min_val="a", max_val="c") is True


@pytest.mark.negative
def test_between_invalid_returns_validation_error():
    assert isinstance(validators.between(99, min_val=1, max_val=10), validators.ValidationError)
