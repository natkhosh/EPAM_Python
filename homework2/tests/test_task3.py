from typing import List, Tuple

import pytest

from homework2.task_3.task_3 import combinations


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (([1, 2], [3, 4]), [[1, 3], [1, 4], [2, 3], [2, 4]]),
        (
            (["a", "b"], ["c", "d"], ["e", "f"]),
            [
                ["a", "c", "e"],
                ["a", "c", "f"],
                ["a", "d", "e"],
                ["a", "d", "f"],
                ["b", "c", "e"],
                ["b", "c", "f"],
                ["b", "d", "e"],
                ["b", "d", "f"],
            ],
        ),
    ],
)
def test_combinations(value: Tuple[List], expected_result: List[List]):
    """
    Testing that function actual returns all possible combinations of items
    from function's arguments.
    """
    assert combinations(*value) == expected_result
