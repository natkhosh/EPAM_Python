"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
import itertools
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    """
    Function takes K lists as arguments and returns all possible lists of
    K items, where the first element is from the first list, the second is
    from the second and so one.

    :param args: lists of any elements as arguments
    :return: list of all possible combinations of items from function's
    arguments.
    """
    return [list(row) for row in itertools.product(*args)]
