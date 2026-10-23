
"""CSV-driven tests for the length validator."""

import csv
from pathlib import Path

import pytest
from validators import ValidationError, length


CSV_FILE = Path(__file__).parent.parent / "data" / "length_cases.csv"


def load_length_cases():
    with CSV_FILE.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


@pytest.mark.member_b
@pytest.mark.datadriven
@pytest.mark.parametrize("case", load_length_cases(), ids=lambda case: case["test_id"])
def test_length_from_csv(case):
    text = case["text"]
    min_val = int(case["min_val"])
    max_val = int(case["max_val"])
    expected = case["expected"] == "True"

    result = length(text, min_val=min_val, max_val=max_val)

    if expected:
        assert result is True
    else:
        assert isinstance(result, ValidationError)


@pytest.mark.member_b
def test_length_with_only_minimum():
    assert length("hello", min_val=3) is True


@pytest.mark.member_b
def test_length_with_only_maximum():
    assert length("hi", max_val=3) is True


@pytest.mark.member_b
def test_length_counts_spaces_and_unicode():
    assert length(" é ", min_val=3, max_val=3) is True
