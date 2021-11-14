from typing import List, Tuple

import pytest

from homework2.task_2.task_2 import *


@pytest.mark.parametrize(
    "value, expected_result",
    [
        ([3, 2, 3], (3, 2)),
        ([1, 1, 2, 4, 5, 2], (2, 4)),
        ([0], (0, 0)),
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
    ],
)
def test_gmajor_and_minor_elem(value: List, expected_result: Tuple[int, int]):
    """
    Testing that function actual finds 10 longest words consisting from largest amount of unique symbols.
    """
    assert major_and_minor_elem(value) == expected_result
