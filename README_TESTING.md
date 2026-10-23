# Assignment 3 - Unit Test Automation (python-validators)

## Setup
```
git clone <GROUP_REPO_URL> && cd validators
python -m venv .venv
# Windows: .venv\Scripts\activate      Mac/Linux: source .venv/bin/activate
pip install -e .
pip install -r requirements-test.txt
```
## Run
| Goal | Command |
|---|---|
| Everything (ordered groups) | `pytest` |
| In parallel (all CPU cores) | `pytest -n auto` |
| Smoke suite only | `pytest -m smoke` |
| ECP / BVA / negative / data-driven | `pytest -m ecp`, `-m bva`, `-m negative`, `-m datadriven` |
| One member only | `pytest -m member_a` / `pytest -m member_b` |
| Combine | `pytest -m "member_a and bva" -n 4` |
| HTML-free summary | `pytest -v` |

## Groups & order
Markers (defined in `pytest.ini`): smoke, ecp, bva, negative, datadriven, member_a, member_b.
Execution order (set in `assignment_tests/conftest.py`): smoke -> ecp -> bva -> negative -> datadriven -> rest.
Parametrization: `@pytest.mark.parametrize` everywhere; CSV-driven tests read `assignment_tests/data/*.csv`.
