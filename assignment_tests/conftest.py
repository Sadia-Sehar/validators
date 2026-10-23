import csv
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


def load_csv(name):
    """Read a CSV from assignment_tests/data and return a list of dict rows."""
    with open(DATA_DIR / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# ---- Task 4: execution order of test groups ----
# smoke -> ecp -> bva -> negative -> datadriven -> everything else
GROUP_ORDER = ["smoke", "ecp", "bva", "negative", "datadriven"]


def _rank(item):
    for i, name in enumerate(GROUP_ORDER):
        if name in item.keywords:
            return i
    return len(GROUP_ORDER)


def pytest_collection_modifyitems(items):
    items.sort(key=_rank)  # stable sort keeps file order inside each group
