"""Member B - Task 3: data-driven tests; data comes from data/length_cases.csv."""
import pytest
import validators
from assignment_tests.conftest import load_csv

pytestmark = [pytest.mark.member_b, pytest.mark.datadriven]
ROWS = load_csv("length_cases.csv")


@pytest.mark.parametrize("row", ROWS, ids=[r["test_id"] for r in ROWS])
def test_length_from_csv(row):
    expected = row["expected"] == "True"
    result = validators.length(row["text"], min_val=int(row["min_val"]), max_val=int(row["max_val"]))
    assert bool(result) is expected, row["description"]
