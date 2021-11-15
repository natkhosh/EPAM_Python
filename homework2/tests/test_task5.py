import string
from typing import Any, Iterable, List

import pytest

from homework2.task_5.task_5 import *


@pytest.mark.parametrize(
    "value, stop, expected_result",
    [
        (string.ascii_lowercase, "g", ["a", "b", "c", "d", "e", "f"]),
        ([66.25, -1, 333, 1, 1234.5, 337], 1, [66.25, -1, 333]),
        ({0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}, 6, [0, 1, 2, 3, 4, 5]),
    ],
)
def test_custom_range(value: Iterable, stop, expected_result: List[Any]):
    assert custom_range(value, stop) == expected_result


@pytest.mark.parametrize(
    "value, start, end, expected_result",
    [
        (
            string.ascii_lowercase,
            "g",
            "p",
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        ([66.25, -1, 333, 1, 1234.5, 337], 1, 337, [1, 1234.5]),
        ({0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}, 2, 6, [2, 3, 4, 5]),
    ],
)
def test_custom_range(value: Iterable, start, end, expected_result: List[Any]):
    assert custom_range(value, start, end) == expected_result


@pytest.mark.parametrize(
    "value, start, end, step, expected_result",
    [
        (string.ascii_lowercase, "p", "g", -2, ["p", "n", "l", "j", "h"]),
        ([66.25, -1, 333, 1, 1234.5, 337], 337, 1, -1, [337, 1234.5]),
        ({0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}, 6, 2, -2, [6, 4]),
    ],
)
def test_custom_range(value: Iterable, start, end, step, expected_result: List[Any]):
    assert (
        custom_range(
            value,
            start,
            end,
            step,
        )
        == expected_result
    )
