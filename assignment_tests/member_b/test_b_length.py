"""Member B - Module 3 (length.py): function length."""
import pytest
import validators

pytestmark = pytest.mark.member_b


@pytest.mark.smoke
@pytest.mark.ecp
def test_length_inside_range():
    assert validators.length("abc", min_val=1, max_val=5) is True


@pytest.mark.bva
@pytest.mark.parametrize("text,expected", [
    ("", False), ("a", True), ("ab", True), ("abcd", True), ("abcde", True), ("abcdef", False),
])
def test_length_boundaries_1_to_5(text, expected):
    assert bool(validators.length(text, min_val=1, max_val=5)) is expected


@pytest.mark.bva
def test_length_empty_string_allowed_when_min_zero():
    assert validators.length("", min_val=0) is True


@pytest.mark.bva
def test_length_exact_size_when_min_equals_max():
    assert validators.length("abc", min_val=3, max_val=3) is True


@pytest.mark.bva
def test_length_exact_size_mismatch_fails():
    assert not validators.length("abcd", min_val=3, max_val=3)


@pytest.mark.negative
def test_length_min_greater_than_max_invalid():
    assert not validators.length("abc", min_val=5, max_val=1)


@pytest.mark.ecp
def test_length_only_min_fails_when_too_short():
    assert not validators.length("abc", min_val=4)


@pytest.mark.ecp
def test_length_only_max_fails_when_too_long():
    assert not validators.length("abc", max_val=2)


def test_length_no_limits_always_valid():
    assert validators.length("abc") is True


@pytest.mark.ecp
def test_length_unicode_counts_characters():
    assert validators.length("héllo", min_val=5, max_val=5) is True


def test_length_spaces_count():
    assert validators.length("a b", min_val=3, max_val=3) is True


@pytest.mark.negative
def test_length_invalid_returns_validation_error():
    assert isinstance(validators.length("abcdef", max_val=3), validators.ValidationError)

@pytest.mark.bva
def test_length_empty_string_with_zero_min_and_max():
    # my own test: 0 to 0 only allows an empty string
    assert validators.length("", min_val=0, max_val=0) is True


@pytest.mark.bva
def test_length_one_character_fails_when_max_is_zero():
    # my own test: one above the maximum
    result = validators.length("a", min_val=0, max_val=0)
    assert isinstance(result, validators.ValidationError)


@pytest.mark.negative
def test_length_negative_min_is_invalid():
    # my own test: negative limits are not allowed
    result = validators.length("abc", min_val=-1)
    assert isinstance(result, validators.ValidationError)