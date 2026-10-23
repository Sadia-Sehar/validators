
from validators import ValidationError, ipv6


def test_valid_ipv6():
    result = ipv6("2001:db8::1", cidr=False)
    assert result is True


def test_invalid_ipv6():
    result = ipv6("abc.0.0.1", cidr=False)
    assert isinstance(result, ValidationError)


def test_ipv6_loopback():
    result = ipv6("::1", cidr=False)
    assert result is True


def test_ipv6_cidr():
    result = ipv6("2001:db8::/32")
    assert result is True


def test_invalid_ipv6_cidr():
    result = ipv6("not-an-ip/32")
    assert isinstance(result, ValidationError)
