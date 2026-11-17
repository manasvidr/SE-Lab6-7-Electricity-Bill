"""Property-based fuzz tests and regression tests for Lab 7."""
import math
import pytest
from hypothesis import given, strategies as st
from electricity_bill import units_consumed, daily_average, tariff_rate

# Fuzz arbitrary strings and non-string values. The functions must either
# return a valid result or reject the input consistently with ValueError.
@given(st.one_of(st.text(), st.none(), st.integers()))
def test_units_consumed_fuzz(value):
    try:
        result = units_consumed(value)
        assert isinstance(result, int) and result >= 0
    except ValueError:
        pass

@given(st.one_of(st.text(), st.none(), st.integers()))
def test_daily_average_fuzz(value):
    try:
        result = daily_average(value)
        assert isinstance(result, (int, float))
        assert math.isfinite(result) and result >= 0
    except ValueError:
        pass

@given(st.one_of(st.text(), st.none(), st.integers()))
def test_tariff_rate_fuzz(value):
    try:
        result = tariff_rate(value)
        assert result in (3, 6, 12)
    except ValueError:
        pass

@given(previous=st.integers(min_value=0, max_value=10**9),
       extra=st.integers(min_value=0, max_value=10**9))
def test_units_consumed_valid_readings(previous, extra):
    assert units_consumed(f"{previous}:{previous + extra}") == extra

@given(values=st.lists(st.integers(min_value=0, max_value=10**6), min_size=1, max_size=50))
def test_daily_average_valid_values(values):
    assert daily_average(",".join(map(str, values))) == round(sum(values) / len(values), 2)

@pytest.mark.parametrize("code,expected", [
    ("DOM-A", 3), ("DOM-B", 6), ("COM-A", 6), ("COM-B", 12),
    ("dom-a", 3), (" COM - B ", 12),
])
def test_tariff_rate_valid_codes(code, expected):
    assert tariff_rate(code) == expected

@pytest.mark.parametrize("reading", [
    "", "1", "1:2:3", ":2", "1:", "a:2", "1:b", "-1:2",
    "2:1", "1.5:2", "1::2",
])
def test_units_consumed_rejects_malformed_readings(reading):
    with pytest.raises(ValueError):
        units_consumed(reading)

@pytest.mark.parametrize("csv", [
    "", ",", "1,,2", "1,", ",1", "a,2", "-1,2", "1.5,2",
])
def test_daily_average_rejects_malformed_csv(csv):
    with pytest.raises(ValueError):
        daily_average(csv)

@pytest.mark.parametrize("code", [
    "", "DOM", "DOM-A-B", "XXX-A", "DOM-Z", "-A", "DOM-", "DOM_A",
])
def test_tariff_rate_rejects_malformed_codes(code):
    with pytest.raises(ValueError):
        tariff_rate(code)

@pytest.mark.parametrize("function,value", [
    (units_consumed, None), (daily_average, None), (tariff_rate, None),
    (units_consumed, 123), (daily_average, 123), (tariff_rate, 123),
])
def test_functions_reject_non_string_inputs(function, value):
    with pytest.raises(ValueError):
        function(value)
