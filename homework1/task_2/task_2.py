"""
Given a cell with "it's a fib sequence" from slideshow,
please write function "check_fib", which accepts a Sequence of integers, and
returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.
"""
import math
from typing import Sequence


def isPerfectSquare(x: int) -> bool:
    """
    A utility function that returns true if x is perfect square
    :param x: integer number
    :return: bool: true for success if x is perfect square, False otherwise.
    """
    s = int(math.sqrt(x))
    return s * s == x


def isFibonacci(n: int) -> bool:
    """
    Function checking if a number is Fibonacci.
    n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both is a perferct square.
    :param n: integer number to check
    :return: bool:Returns true if n is a Fibonacci Number, else false
    """
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)


def check_fibonacci(data: Sequence[int]) -> bool:
    """
    Function for check a Fibonacci sequence.
    :param data: Sequence of integers
    :return: bool: true for success if the given sequence is a Fibonacci sequence, False otherwise.
    """
    if len(data) < 2:
        return False
    elif len(data) < 3:
        for i in range(1, len(data)):
            if not (
                (data[i - 1] <= data[i])
                and isFibonacci(data[i - 1])
                and isFibonacci(data[i])
                and isFibonacci(data[i - 1] + data[i])
            ):
                return False
        return True
    else:
        if (data[0] < data[1]) and isFibonacci(data[0]) and isFibonacci(data[1]):
            for i in range(2, len(data)):
                if data[i] != data[i - 1] + data[i - 2]:
                    return False
            return True
        return False
