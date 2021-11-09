from typing import List

import pytest

from homework1.task_5.task_5 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    "value, subarray_len, expected_result",
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([-2, 22, 0, -3, 5, 3, 6, 7], 3, 22),
        ([1, 3, -1, -3, 5, 3, 6, 7], 5, 18),
        ([1, 3, -1, -3, 5, 3], 6, 8),
        ([1, 3, -1, -3, 5, 3], 7, 0),
        ([1, 3, -1], -1, 0),
        ([], 3, 0),
        ([], 0, 0),
    ],
)
def test_find_maximal_subarray_sum(
    value: List[int], subarray_len: int, expected_result: int
):
    """
    Testing that function finds a sub-array with length less then or equal to "k", with maximal sum.
    """
    assert find_maximal_subarray_sum(value, subarray_len) == expected_result
