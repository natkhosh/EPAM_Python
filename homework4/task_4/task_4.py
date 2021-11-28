"""
Write a function that takes a number N as an input and returns N FizzBuzz
numbers*
Write a doctest for that function.

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests


assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть
картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Function takes a number N as an input and returns N FizzBuzz numbers.
    Any number divisible by three is replaced by the word fizz.
    Any number divisible by five by the word buzz.
    Numbers divisible by 15 become fizz buzz.
    :param n: length of Fizzbuzz sequence
    :return: list: Fizzbuzz sequence

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', \
'fizz', '13', '14', 'fizzbuzz']
    >>> fizzbuzz(1)
    ['1']
    >>> fizzbuzz(0)
    Traceback (most recent call last):
    ...
    ValueError: n must be integer and not less than 1
    >>> fizzbuzz(1.5)
    Traceback (most recent call last):
    ...
    ValueError: n must be integer and not less than 1

    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be integer and not less than 1")

    result = []
    for number in range(1, n + 1):
        if number % 15 == 0:
            result.append("fizzbuzz")
        elif number % 3 == 0:
            result.append("fizz")
        elif number % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(number))
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
