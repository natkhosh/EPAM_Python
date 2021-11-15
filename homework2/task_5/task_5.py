"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Any, Iterable, List


def custom_range(iterable: Iterable, start, stop=None, step=1) -> List[Any]:
    if isinstance(iterable, dict):
        iterable_1 = [k for (k, v) in iterable.items()]
    else:
        iterable_1 = iterable

    result = []
    start = iterable_1.index(start)
    if stop is None:
        for i in range(0, start, step):
            result.append(iterable_1[i])
        return result
    else:
        stop = iterable_1.index(stop)
        for i in range(start, stop, step):
            result.append(iterable_1[i])
        return result
