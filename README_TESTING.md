# Assignment 3 - Unit Test Automation (python-validators)

## Setup

```
git clone <GROUP\_REPO\_URL> \&\& cd validators
python -m venv .venv
# Windows: .venv\\Scripts\\activate      Mac/Linux: source .venv/bin/activate
pip install -e .
pip install -r requirements-test.txt
```

## Run

|Goal|Command|
|-|-|
|Everything (ordered groups)|`pytest`|
|In parallel (all CPU cores)|`pytest -n auto`|
|Smoke suite only|`pytest -m smoke`|
|ECP / BVA / negative / data-driven|`pytest -m ecp`, `-m bva`, `-m negative`, `-m datadriven`|
|One member only|`pytest -m member\_a` / `pytest -m member\_b`|
|Combine|`pytest -m "member\_a and bva" -n 4`|
|Verbose list of every test|`pytest -v`|
|Coverage of the four tested modules|`pytest --cov=validators.utils --cov=validators.ip\_address --cov=validators.between --cov=validators.length --cov-report=term-missing`|

## Groups \& order

Markers (defined in `pytest.ini`): smoke, ecp, bva, negative, datadriven, member\_a, member\_b.
Execution order (set in `assignment\_tests/conftest.py`): smoke -> ecp -> bva -> negative -> datadriven -> rest.
The order is guaranteed when running without `-n`; with `-n` the tests are distributed across workers.
Parametrization: `@pytest.mark.parametrize` everywhere; CSV-driven tests read `assignment\_tests/data/\*.csv`.

## Documents

* `docs/ECP\_BVA\_Notes.md` - ECP/BVA analysis per module
* `docs/Task3\_Test\_Cases.xlsx` - Excel test cases linked to the CSV data files
* `docs/Summary\_Report.docx` - summary report
* `docs/validators\_setup\_video.mp4` - environment setup video

