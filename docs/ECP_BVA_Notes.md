# ECP & BVA Notes - python-validators (v0.36.0)

Group modules: **utils.py**, **ip_address.py**, **between.py + length.py**.
Member A = Sadia Sehar (24F-3123). Member B = Azka Nadeem (24P-3042).
Test oracle = observed behaviour of the library source in this repository + its docstrings. Every case below was executed (182 tests, all passing).

Techniques used: **ECP** (Equivalence Class Partitioning) - one representative value per class of inputs that the code treats the same way; **BVA** (Boundary Value Analysis) - values just below, on, and just above each limit.

## Module 1 - utils.py
### Member A: class `ValidationError` (`__init__`, `__repr__`, `__str__`, `__bool__`)
File: `member_a/test_a_validation_error.py` (27 test cases)

| Method | ECP classes | BVA points |
|---|---|---|
| `__init__` | with message / without message; extra argument names become attributes | message `""` (empty = no `reason`), arg_dict `{}` |
| `__repr__` | normal args, empty args | `{}` args; `func` must be excluded from args |
| `__str__` | any value type (0, "", None, [], str, float) | equals `repr` |
| `__bool__` | always False (with/without message, any args) | empty args |

Also checked: it is a subclass of `Exception` and can be raised and caught.

### Member B: decorator `@validator`
File: `member_b/test_b_validator_decorator.py` (30 test cases)
ECP: truthy return -> `True`; falsy -> `ValidationError`; ValueError/TypeError/UnicodeError -> `ValidationError` with `reason`; other exceptions propagate.
Raise mode: `r_ve=True` raises; `r_ve=False` does **not** raise (the repository source respects a false value; the older PyPI 0.36.0 package treated the mere presence of `r_ve` as "raise", so this test was written against the repository source). Environment variable `RAISE_VALIDATION_ERROR` == exactly `"True"` raises; "False", "false", "1", "yes", "" do not.
BVA: even numbers 0, 2, -4 (zero, negative); odd 1, -3.
Added by Member B: two arguments are recorded in the `ValidationError`; the returned error is falsy; env variable `"True"` with valid input still returns `True`.

## Module 2 - ip_address.py
### Member A: `ipv4`
Files: `member_a/test_a_ipv4.py` (35 test cases), `member_a/test_a_csv_ipv4.py` (8 cases from `ipv4_cases.csv`)
- Octet range 0-255: valid 0, 255; invalid 256, -1, 999. Leading zero `01.2.3.4` invalid.
- Octet count: valid 4; invalid 1, 2, 3, 5.
- CIDR prefix 0-32: valid /0, /1, /32; invalid /33. `cidr=False` rejects CIDR.
- `private=True/False` filter: 10.0.0.1 (private) vs 8.8.8.8 (public).
- `strict=True`: requires CIDR notation.
- Malformed: empty, leading/trailing space, letters.
- Error handling: invalid input returns a `ValidationError` object; `r_ve=True` raises it.

### Member B: `ipv6`
File: `member_b/test_b_ipv6.py` (30 test cases)
- Group count: valid 8 groups; invalid 7 (no `::`) and 9. Group length max 4 hex digits (`12345::1` invalid).
- Compression `::`: valid once (`::1`, `::`); invalid twice (`1::2::3`).
- CIDR prefix 0-128: valid /0, /64, /128; invalid /129. `cidr=False`, `strict=True` as in ipv4.
- IPv4-mapped `::ffff:192.168.1.1` valid; plain IPv4 invalid; bad hex `g` invalid.
- Added by Member B: `::` at the end of an address is valid, uppercase hex digits are valid, a non-numeric CIDR prefix is invalid.

## Module 3 - between.py / length.py
### Member A: `between(value, min_val, max_val)` (range 1..10)
File: `member_a/test_a_between.py` (23 test cases)
BVA (3-value + inclusive): 0 F, 1 T, 2 T, 9 T, 10 T, 11 F. Equal limits (5,5). min > max -> invalid.
ECP: only min, only max, no limits, negatives, floats, strings (alphabetical).

### Member B: `length(value, min_val, max_val)` (range 1..5)
Files: `member_b/test_b_length.py` (20 test cases), `member_b/test_b_csv_length.py` (9 cases from `length_cases.csv`)
BVA: len 0 F, 1 T, 2 T, 4 T, 5 T, 6 F. min=0 allows "", min=max exact length, min > max invalid.
ECP: only min, only max, no limits, unicode chars (count characters), spaces count.
Added by Member B: a negative `min_val` is invalid; a 1-character string fails when `max_val=0`; an empty string is valid when `min_val=0` and `max_val=0`; extra CSV rows TC_B08 and TC_B09 for the zero-length boundary.

## Task 3 data files
`assignment_tests/data/ipv4_cases.csv` (Member A, 8 rows), `assignment_tests/data/length_cases.csv` (Member B, 9 rows).
The matching test cases are listed in `docs/Task3_Test_Cases.xlsx` (sheets `Member_A_ipv4` and `Member_B_length`).

## Summary of test counts
| Member | Test cases | Files |
|---|---|---|
| A | 93 | `test_a_validation_error.py` 27, `test_a_ipv4.py` 35, `test_a_between.py` 23, `test_a_csv_ipv4.py` 8 |
| B | 89 | `test_b_validator_decorator.py` 30, `test_b_ipv6.py` 30, `test_b_length.py` 20, `test_b_csv_length.py` 9 |
| **Total** | **182** | |
