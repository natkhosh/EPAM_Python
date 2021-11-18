from typing import Callable, Tuple

import pytest

from homework2.task_4.task_4 import cache


@pytest.mark.parametrize(
    "test_input, some_func, expected_result",
    [
        ((100, 200), (lambda a, b: (a ** b) ** 2), True),
        ((1, 2, 3), (lambda a, b, c: (a + b) * c), True),
    ],
)
def test_cache(test_input: Tuple[int],
               some_func: Callable,
               expected_result: bool):
    """
    Testing that call to function was cached.
    """
    func_cache = cache(some_func)
    val_1 = func_cache(*test_input)
    val_2 = func_cache(*test_input)
    result = val_1 is val_2

    assert result == expected_result
