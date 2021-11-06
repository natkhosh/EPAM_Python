import pytest

from homework1.sample_project.calculator.calc import check_power_of_2


@pytest.mark.parametrize(
    "a, expected_result", [(65536, True), (12, False), (0, False), (1, True)]
)
def test_positive_case(a, expected_result):
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(a) == expected_result
