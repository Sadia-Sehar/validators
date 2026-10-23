# ECP & BVA Notes - python-validators (v0.36.0)

Group modules: **utils.py**, **ip_address.py**, **between.py + length.py**.
Test oracle = observed behaviour of the library + its docstrings. Every case below was executed.

## Module 1 - utils.py
### Member A: class `ValidationError` (`__init__`, `__repr__`, `__str__`, `__bool__`)
| Method | ECP classes | BVA points |
|---|---|---|
| `__init__` | with message / without message | message `""` (empty = no `reason`), arg_dict `{}` |
| `__repr__` | normal args, empty args | `{}` args; `func` must be excluded from args |
| `__str__` | any value type (0, "", None, [], str, float) | equals `repr` |
| `__bool__` | always False (with/without message, any args) | empty args |
### Member B: decorator `@validator`
ECP: truthy return -> `True`; falsy -> `ValidationError`; ValueError/TypeError/UnicodeError -> `ValidationError` with `reason`; other exceptions propagate.
Raise mode: `r_ve` kwarg (ANY value enables it - key presence), env `RAISE_VALIDATION_ERROR` == exactly `"True"`; "False","false","1","yes","" do not.
BVA: even numbers 0, 2, -4 (zero, negative); odd 1, -3.

## Module 2 - ip_address.py
### Member A: `ipv4`
- Octet range 0-255: valid 0, 255; invalid 256, -1, 999. Leading zero `01.2.3.4` invalid.
- Octet count: valid 4; invalid 1, 2, 3, 5.
- CIDR prefix 0-32: valid /0, /1, /32; invalid /33. `cidr=False` rejects CIDR.
- `private=True/False` filter: 10.0.0.1 (private) vs 8.8.8.8 (public).
- `strict=True`: requires CIDR notation.
- Malformed: empty, leading/trailing space, letters.
### Member B: `ipv6`
- Group count: valid 8 groups; invalid 7 (no `::`) and 9. Group length max 4 hex digits (`12345::1` invalid).
- Compression `::`: valid once (`::1`, `::`); invalid twice (`1::2::3`).
- CIDR prefix 0-128: valid /0, /64, /128; invalid /129. `cidr=False`, `strict=True` as in ipv4.
- IPv4-mapped `::ffff:192.168.1.1` valid; plain IPv4 invalid; bad hex `g` invalid.

## Module 3 - between.py / length.py
### Member A: `between(value, min_val, max_val)` (range 1..10)
BVA (3-value + inclusive): 0 F, 1 T, 2 T, 9 T, 10 T, 11 F. Equal limits (5,5). min > max -> invalid.
ECP: only min, only max, no limits, negatives, floats, strings (alphabetical).
### Member B: `length(value, min_val, max_val)` (range 1..5)
BVA: len 0 F, 1 T, 2 T, 4 T, 5 T, 6 F. min=0 allows "", min=max exact length, min > max invalid.
ECP: only min, only max, no limits, unicode chars (count characters), spaces count.

## Task 3 data files
`assignment_tests/data/ipv4_cases.csv` (Member A), `length_cases.csv` (Member B).
