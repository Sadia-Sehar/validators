
import pytest

from validators import ValidationError, length


@pytest.mark.member_b
def test_length_valid_text():
    assert length("hello", min_val=1, max_val=10) is True


@pytest.mark.member_b
def test_length_below_minimum():
    result = length("hi", min_val=3)
    assert isinstance(result, ValidationError)


@pytest.mark.member_b
def test_length_above_maximum():
    result = length("hello", max_val=3)
    assert isinstance(result, ValidationError)

@pytest.mark.member_b
def test_length_exact_minimum():
    assert length("abc", min_val=3) is True


@pytest.mark.member_b
def test_length_exact_maximum():
    assert length("abc", max_val=3) is True
