"""Member B - Module 1 (utils.py): the @validator decorator."""
import pytest
from validators import ValidationError, validator

pytestmark = pytest.mark.member_b


@validator
def even(value):
    return not (value % 2)


@pytest.mark.smoke
def test_decorated_returns_true_when_function_truthy():
    assert even(4) is True


@pytest.mark.smoke
def test_decorated_returns_validation_error_when_falsy():
    assert isinstance(even(5), ValidationError)


@pytest.mark.ecp
@pytest.mark.parametrize("n", [0, 2, 100, -4])
def test_even_numbers_valid(n):
    assert even(n) is True


@pytest.mark.ecp
@pytest.mark.parametrize("n", [1, 3, 101, -3])
def test_odd_numbers_invalid(n):
    assert not even(n)


def test_decorator_preserves_function_name():
    assert even.__name__ == "even"


def test_validation_error_records_function():
    assert even(5).func.__name__ == "even"


def test_validation_error_records_argument_value():
    assert even(5).value == 5


@pytest.mark.negative
def test_r_ve_true_raises_on_failure():
    with pytest.raises(ValidationError):
        even(5, r_ve=True)


def test_r_ve_true_returns_true_on_success():
    assert even(4, r_ve=True) is True


@pytest.mark.negative
def test_r_ve_false_does_not_raise():
    # source behaviour: r_ve=False is treated as False, so no exception is raised
    result = even(5, r_ve=False)
    assert isinstance(result, ValidationError)


@pytest.mark.negative
def test_env_variable_true_raises(monkeypatch):
    monkeypatch.setenv("RAISE_VALIDATION_ERROR", "True")
    with pytest.raises(ValidationError):
        even(5)


@pytest.mark.ecp
@pytest.mark.parametrize("env", ["False", "false", "1", "yes", ""])
def test_env_variable_other_values_do_not_raise(monkeypatch, env):
    monkeypatch.setenv("RAISE_VALIDATION_ERROR", env)
    assert isinstance(even(5), ValidationError)


@pytest.mark.negative
def test_type_error_is_converted_to_validation_error():
    result = even("text")  # "text" % 2 raises TypeError inside
    assert isinstance(result, ValidationError)


def test_type_error_stores_reason():
    assert hasattr(even("text"), "reason")


@pytest.mark.negative
def test_type_error_with_r_ve_raises_validation_error():
    with pytest.raises(ValidationError):
        even("text", r_ve=True)


def test_works_with_keyword_argument():
    assert even(value=4) is True


def test_unexpected_exception_type_is_not_swallowed():
    @validator
    def boom(value):
        raise KeyError("x")
    with pytest.raises(KeyError):
        boom(1)

@validator
def greater_than(a, b):
    return a > b


@pytest.mark.ecp
def test_two_arguments_are_recorded_in_validation_error():
    # my own test: both arguments should be stored on the error object
    result = greater_than(1, 2)
    assert isinstance(result, ValidationError)
    assert result.a == 1
    assert result.b == 2


@pytest.mark.negative
def test_env_variable_true_with_valid_input_returns_true(monkeypatch):
    # my own test: raise mode must not break valid input
    monkeypatch.setenv("RAISE_VALIDATION_ERROR", "True")
    assert even(4) is True


@pytest.mark.smoke
def test_validation_error_is_falsy():
    # my own test: a failed validation can be used directly in an if statement
    assert bool(even(5)) is False