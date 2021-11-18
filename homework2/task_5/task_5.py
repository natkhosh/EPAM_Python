"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g')
        == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p')
        == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2)
        == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Any, Iterable, List


def custom_range(iterable: Iterable, *args) -> List[Any]:
    """
    Function accepts iterable of unique values, start index,
    end index and step and behaves behaves as range function.
    :param iterable: any iterable of unique values
    :param start: Optional - it is the starting position of the sequence
    (Lower limit)
    :param stop: Required — an element that specifies where to stop
    (Upper limit)
    :param step: Optional — an element that specifies how much to increment
    the element (Default value is 1)
    :return: List of values depend on recieved arguments
    """
    iterable_arr = [k for (k, v) in iterable.items()] \
        if isinstance(iterable, dict) else iterable

    result = []

    if len(args) == 1:
        stop = iterable_arr.index(args[0])
        for i in range(0, stop):
            result.append(iterable_arr[i])
    elif len(args) == 2:
        start, stop = args
        for i in range(iterable_arr.index(start), iterable_arr.index(stop)):
            result.append(iterable_arr[i])
    elif len(args) == 3:
        start, stop, custom_step = args
        for i in range(
            iterable_arr.index(start), iterable_arr.index(stop), custom_step
        ):
            result.append(iterable_arr[i])
    else:
        raise TypeError("Too many arguments for range function")
    return result
