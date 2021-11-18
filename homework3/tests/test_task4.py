import pytest

from homework3.task_4.task_4 import is_armstrong


@pytest.mark.parametrize('value, expected_result', [(153, True), (10, False)])
def test_is_armstrong(value: int, expected_result: bool):
    """
    Testing that function detects if a number is Armstrong number.
    """
    assert is_armstrong(value) == expected_result
