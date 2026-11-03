"""Decision/branch-coverage tests for the electricity bill application (Lab 6)."""
import pytest
from electricity_bill import energy_charge, late_fee, subsidy


@pytest.mark.parametrize("connection", ["domestic", "commercial"])
def test_connection_branch(connection):
    expected = 200 if connection == "domestic" else 450
    assert energy_charge(50, connection) == expected


def test_unknown_connection_branch():
    with pytest.raises(ValueError, match="unknown connection"):
        energy_charge(50, "industrial")


def test_negative_units_branch():
    with pytest.raises(ValueError, match="invalid units"):
        energy_charge(-1, "domestic")


@pytest.mark.parametrize(
    "units,expected",
    [(100, 350), (101, 355), (300, 1350), (301, 1358)],
)
def test_each_energy_slab_branch(units, expected):
    assert energy_charge(units, "domestic") == expected


@pytest.mark.parametrize("days,expected", [(0, 0), (-2, 0), (1, 50), (15, 50), (16, 100)])
def test_late_fee_delay_branches(days, expected):
    assert late_fee(1000, days) == expected


def test_late_fee_bill_threshold_false():
    assert late_fee(2000, 16) == 100


def test_late_fee_bill_threshold_true():
    assert late_fee(2001, 16) == 200


@pytest.mark.parametrize(
    "units,senior,expected",
    [(100, True, 50), (101, True, 0), (100, False, 0)],
)
def test_senior_and_unit_threshold_branches(units, senior, expected):
    assert subsidy(units, senior, False) == expected


def test_solar_branch_and_units_not_over_300():
    assert subsidy(300, False, True) == 100


def test_solar_branch_and_units_over_300_resets_total():
    assert subsidy(301, True, True) == 0


def test_no_solar_no_senior():
    assert subsidy(301, False, False) == 0
