"""Task 3: data-driven tests; data comes from data/ipv4_cases.csv."""
import pytest
import validators
from assignment_tests.conftest import load_csv

pytestmark = [pytest.mark.member_a, pytest.mark.datadriven]
ROWS = load_csv("ipv4_cases.csv")


@pytest.mark.parametrize("row", ROWS, ids=[r["test_id"] for r in ROWS])
def test_ipv4_from_csv(row):
    expected = row["expected"] == "True"
    assert bool(validators.ipv4(row["input"])) is expected, row["description"]
