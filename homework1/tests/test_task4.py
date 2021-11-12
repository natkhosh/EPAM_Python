from typing import List

import pytest

from homework1.task_4.task_4 import check_sum_of_four


@pytest.mark.parametrize(
    "a, b, c, d, expected_result",
    [
        ([1, 2], [-2, -1], [-1, 2], [0, 2], 2),
        ([0, 1], [-1, 0], [1, 0], [0, -1], 3),
        ([0], [0], [0], [0], 1),
    ],
)
def test_check_sum_of_four(
    a: List[int], b: List[int], c: List[int], d: List[int], expected_result: int
):
    """
    Testing that function computes how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
    """
    assert check_sum_of_four(a, b, c, d) == expected_result
