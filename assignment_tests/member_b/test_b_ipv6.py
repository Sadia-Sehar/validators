"""Member B - Module 2 (ip_address.py): function ipv6."""
import pytest
import validators

pytestmark = pytest.mark.member_b


@pytest.mark.smoke
@pytest.mark.ecp
@pytest.mark.parametrize("ip", [
    "::1", "::", "2001:db8::1", "2001:0db8:85a3:0000:0000:8a2e:0370:7334", "fe80::1",
])
def test_ipv6_valid_addresses(ip):
    assert validators.ipv6(ip) is True


@pytest.mark.bva
@pytest.mark.parametrize("ip,expected", [
    ("1:2:3:4:5:6:7", False),    # 7 groups: one below boundary
    ("1:2:3:4:5:6:7:8", True),   # 8 groups: exact boundary
    ("1:2:3:4:5:6:7:8:9", False),  # 9 groups: one above boundary
])
def test_ipv6_group_count_boundaries(ip, expected):
    assert bool(validators.ipv6(ip)) is expected


@pytest.mark.bva
@pytest.mark.parametrize("ip,expected", [("::1", True), ("12345::1", False), ("ffff::1", True)])
def test_ipv6_group_length_boundary(ip, expected):
    assert bool(validators.ipv6(ip)) is expected


@pytest.mark.negative
@pytest.mark.parametrize("ip", ["", "2001:db8::g", "1::2::3", "not-an-ip", "::1::"])
def test_ipv6_invalid_strings(ip):
    assert not validators.ipv6(ip)


@pytest.mark.bva
@pytest.mark.parametrize("cidr,expected", [("/0", True), ("/64", True), ("/128", True), ("/129", False)])
def test_ipv6_cidr_prefix_boundaries(cidr, expected):
    assert bool(validators.ipv6("::1" + cidr)) is expected


def test_ipv6_cidr_disabled_rejects_cidr():
    assert not validators.ipv6("::1/128", cidr=False)


def test_ipv6_strict_rejects_plain_address():
    assert not validators.ipv6("::1", strict=True)


def test_ipv6_strict_accepts_cidr_address():
    assert validators.ipv6("::1/64", strict=True) is True


def test_ipv6_ipv4_mapped_address_valid():
    assert validators.ipv6("::ffff:192.168.1.1") is True


@pytest.mark.negative
def test_ipv6_invalid_returns_validation_error_object():
    assert isinstance(validators.ipv6("bad"), validators.ValidationError)


@pytest.mark.negative
def test_ipv6_r_ve_raises():
    with pytest.raises(validators.ValidationError):
        validators.ipv6("bad", r_ve=True)


@pytest.mark.negative
def test_ipv6_rejects_ipv4_address():
    assert not validators.ipv6("192.168.1.1")

@pytest.mark.ecp
def test_ipv6_uppercase_hex_is_valid():
    # my own test: hex digits can be capital letters
    assert validators.ipv6("2001:DB8::1") is True


@pytest.mark.bva
def test_ipv6_compressed_at_the_end_is_valid():
    # my own test: "::" at the end covers the last group
    assert validators.ipv6("1:2:3:4:5:6:7::") is True


@pytest.mark.negative
def test_ipv6_non_numeric_cidr_prefix_is_invalid():
    # my own test: prefix must be a number
    result = validators.ipv6("2001:db8::1/abc")
    assert isinstance(result, validators.ValidationError)