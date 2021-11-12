from typing import Sequence

import pytest

from homework1.task_2.task_2 import check_fibonacci


@pytest.mark.parametrize(
    "value, expected_result",
    [
        ([0, 1], True),
        ([1, 1], True),
        ([2, 1], False),
        ([2, 3], True),
        ([1], False),
        ([], False),
        ([10, -5, 5], False),
        ([0, 1, 2, 3, 5, 8], False),
        ([0, 1, 1, 2, 3, 5, 8], True),
        ([377, 610, 987, 1597], True),
    ],
)
def test_check_fibonacci(value: Sequence[int], expected_result: bool):
    """
    Testing that actual given sequence is a Fibonacci sequence
    """
    assert check_fibonacci(value) == expected_result
