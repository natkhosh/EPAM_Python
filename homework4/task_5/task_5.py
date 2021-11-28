"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this
video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


# >>> list(fizzbuzz(5))
# ["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import Generator


def fizzbuzz(n: int) -> Generator[str, None, None]:
    """
    Function takes a number N as an input and returns N FizzBuzz numbers.
    Any number divisible by three is replaced by the word fizz.
    Any number divisible by five by the word buzz.
    Numbers divisible by 15 become fizz buzz.
    :param n: length of Fizzbuzz sequence
    :return: generator: N FizzBuzz numbers


    >>> list(fizzbuzz(5))
    ['1', '2', 'fizz', '4', 'buzz']
    >>> list(fizzbuzz(1))
    ['1']
    >>> list(fizzbuzz(0))
    Traceback (most recent call last):
    ...
    ValueError: n must be integer and not less than 1
    >>> list(fizzbuzz(1.5))
    Traceback (most recent call last):
    ...
    ValueError: n must be integer and not less than 1

    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be integer and not less than 1")

    fizzes = [''] + ([''] * 2 + ['fizz']) * 33 + ['']
    buzzes = [''] + ([''] * 4 + ['buzz']) * 20

    for i in range(1, n + 1):
        result = str(fizzes[i]) + str(buzzes[i]) or str(i)
        yield result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
