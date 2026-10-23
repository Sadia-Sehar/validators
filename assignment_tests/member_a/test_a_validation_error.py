"""Module 1 (utils.py): class ValidationError."""
import pytest
from validators import ValidationError

pytestmark = pytest.mark.member_a


def sample_func(value):
    return value


# ---- __init__ ----
@pytest.mark.smoke
def test_init_stores_function():
    err = ValidationError(sample_func, {"value": 1})
    assert err.func is sample_func


def test_init_stores_args_as_attributes():
    err = ValidationError(sample_func, {"value": 1, "extra": "x"})
    assert err.value == 1 and err.extra == "x"


@pytest.mark.ecp
def test_init_with_message_sets_reason():
    err = ValidationError(sample_func, {"value": 1}, "bad input")
    assert err.reason == "bad input"


@pytest.mark.ecp
def test_init_without_message_has_no_reason():
    err = ValidationError(sample_func, {"value": 1})
    assert not hasattr(err, "reason")


@pytest.mark.bva
def test_init_empty_message_has_no_reason():
    err = ValidationError(sample_func, {"value": 1}, "")
    assert not hasattr(err, "reason")


@pytest.mark.bva
def test_init_empty_arg_dict():
    err = ValidationError(sample_func, {})
    assert err.func is sample_func


# ---- __repr__ ----
@pytest.mark.smoke
def test_repr_contains_function_name():
    assert "func=sample_func" in repr(ValidationError(sample_func, {"value": 1}))


def test_repr_contains_args():
    assert "'value': 1" in repr(ValidationError(sample_func, {"value": 1}))


def test_repr_excludes_func_from_args():
    assert "'func'" not in repr(ValidationError(sample_func, {"value": 1}))


def test_repr_exact_format():
    err = ValidationError(sample_func, {"value": "abc"})
    assert repr(err) == "ValidationError(func=sample_func, args={'value': 'abc'})"


@pytest.mark.bva
def test_repr_empty_args():
    assert repr(ValidationError(sample_func, {})) == "ValidationError(func=sample_func, args={})"


# ---- __str__ ----
def test_str_equals_repr():
    err = ValidationError(sample_func, {"value": 1})
    assert str(err) == repr(err)


def test_str_returns_string_type():
    assert isinstance(str(ValidationError(sample_func, {"value": 1})), str)


@pytest.mark.parametrize("value", [0, "", None, [], "text", 3.14])
def test_str_works_for_many_value_types(value):
    assert "ValidationError" in str(ValidationError(sample_func, {"value": value}))


# ---- __bool__ ----
@pytest.mark.smoke
def test_bool_is_false():
    assert bool(ValidationError(sample_func, {"value": 1})) is False


def test_bool_false_in_if_statement():
    assert not ValidationError(sample_func, {"value": 1})


@pytest.mark.parametrize("arg_dict", [{}, {"value": 1}, {"a": 1, "b": 2}])
def test_bool_false_for_any_args(arg_dict):
    assert not ValidationError(sample_func, arg_dict)


def test_bool_false_even_with_message():
    assert not ValidationError(sample_func, {"value": 1}, "msg")


# ---- inheritance ----
@pytest.mark.smoke
def test_is_subclass_of_exception():
    assert issubclass(ValidationError, Exception)


def test_can_be_raised_and_caught():
    with pytest.raises(ValidationError):
        raise ValidationError(sample_func, {"value": 1})
