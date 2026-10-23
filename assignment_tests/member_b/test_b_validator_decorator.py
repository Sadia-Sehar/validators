
import pytest
from validators import ValidationError
from validators.utils import validator


@validator
def is_even(value):
    return value % 2 == 0


def test_valid_input():
    result = is_even(4)
    assert result is True


def test_invalid_input():
    result = is_even(5)
    assert isinstance(result, ValidationError)


def test_invalid_input_with_r_ve():
    with pytest.raises(ValidationError):
        is_even(5, r_ve=True)


def test_valid_input_with_keyword_argument():
    result = is_even(value=6)
    assert result is True


def test_invalid_input_with_keyword_argument():
    result = is_even(value=7)
    assert isinstance(result, ValidationError)
