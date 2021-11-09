"""
Given a cell with "it's a fib sequence" from slideshow,
please write function "check_fib", which accepts a Sequence of integers, and
returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def _check_window(x: int, y: int, z: int) -> bool:
    """
    Support function to checking sum
    :param x: integer
    :param y: integer
    :param z: integer
    :return: bool
    """
    return (x + y) == z


def check_fibonacci(data: Sequence[int]) -> bool:
    """
    Function for check a Fibonacci sequence.
    :param data: Sequence of integers
    :return: bool: true for success if the given sequence is a Fibonacci sequence, False otherwise.
    """
    if len(data) < 3:
        print("Invalid data")
        return False
    else:
        while len(data) >= 3:
            x, y, z = data[0], data[1], data[2]

            if _check_window(x, y, z):
                data = data[1:]
            else:
                return False
        return True
