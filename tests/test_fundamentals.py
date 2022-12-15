import pytest


def test_valid_periods():
    from fundamentals._utils import _validate_period

    assert "annual" == _validate_period("annual")
    assert "quarter" == _validate_period("quarter")


def test_invalid_period_types():
    from fundamentals._utils import _validate_period

    with pytest.raises(TypeError):
        _validate_period(["Annual"])
        _validate_period({"Quarter": 1})
        _validate_period(66)
        _validate_period(89.12)
        _validate_period(True)


def test_invalid_period_values():
    from fundamentals._utils import _validate_period

    with pytest.raises(ValueError):
        _validate_period("Annual")
        _validate_period("Quarter")
        _validate_period("Annually")
        _validate_period("Quarterly")


def test_valid_limits():
    from fundamentals._utils import _validate_limit

    assert 16 == _validate_limit(16)
    assert 99 == _validate_limit(99)
    assert 1 == _validate_limit(1)
    assert 7 == _validate_limit(7)


def test_invalid_limit_types():
    from fundamentals._utils import _validate_limit

    with pytest.raises(TypeError):
        _validate_limit("Annual")
        _validate_limit(15.0)
        _validate_limit(["Annually"])
        _validate_limit({"Quarterly": 1})
        _validate_limit(False)

    with pytest.raises(ValueError):
        _validate_limit(101)
        _validate_limit(0)
