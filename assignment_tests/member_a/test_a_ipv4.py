"""Module 2 (ip_address.py): function ipv4."""
import pytest
import validators

pytestmark = pytest.mark.member_a


@pytest.mark.smoke
@pytest.mark.ecp
@pytest.mark.parametrize("ip", ["192.168.1.1", "8.8.8.8", "10.0.0.1", "172.16.0.1"])
def test_ipv4_valid_addresses(ip):
    assert validators.ipv4(ip) is True


@pytest.mark.bva
@pytest.mark.parametrize("ip", ["0.0.0.0", "255.255.255.255", "0.0.0.255", "255.0.0.0"])
def test_ipv4_octet_boundaries_valid(ip):
    assert validators.ipv4(ip) is True


@pytest.mark.bva
@pytest.mark.negative
@pytest.mark.parametrize("ip", ["256.1.1.1", "1.1.1.256", "1.1.1.-1", "999.999.999.999"])
def test_ipv4_octet_boundaries_invalid(ip):
    assert not validators.ipv4(ip)


@pytest.mark.negative
@pytest.mark.parametrize("ip", ["1.2.3", "1.2.3.4.5", "1", "1.2"])
def test_ipv4_wrong_octet_count(ip):
    assert not validators.ipv4(ip)


@pytest.mark.negative
@pytest.mark.parametrize("ip", ["", " 1.2.3.4", "a.b.c.d", "01.2.3.4", "1.2.3.4 "])
def test_ipv4_malformed_strings(ip):
    assert not validators.ipv4(ip)


@pytest.mark.bva
@pytest.mark.parametrize("cidr,expected", [("/0", True), ("/1", True), ("/32", True), ("/33", False)])
def test_ipv4_cidr_prefix_boundaries(cidr, expected):
    assert bool(validators.ipv4("192.168.1.0" + cidr)) is expected


def test_ipv4_cidr_disabled_rejects_cidr():
    assert not validators.ipv4("192.168.1.0/24", cidr=False)


def test_ipv4_cidr_enabled_by_default():
    assert validators.ipv4("192.168.1.0/24") is True


@pytest.mark.ecp
@pytest.mark.parametrize("ip,private,expected", [
    ("10.0.0.1", True, True), ("8.8.8.8", True, False),
    ("8.8.8.8", False, True), ("10.0.0.1", False, False),
])
def test_ipv4_private_filter(ip, private, expected):
    assert bool(validators.ipv4(ip, private=private)) is expected


def test_ipv4_strict_rejects_plain_address():
    assert not validators.ipv4("1.2.3.4", strict=True)


def test_ipv4_strict_accepts_cidr_address():
    assert validators.ipv4("1.2.3.4/24", strict=True) is True


@pytest.mark.negative
def test_ipv4_invalid_returns_validation_error_object():
    assert isinstance(validators.ipv4("bad"), validators.ValidationError)


@pytest.mark.negative
def test_ipv4_r_ve_raises():
    with pytest.raises(validators.ValidationError):
        validators.ipv4("bad", r_ve=True)
