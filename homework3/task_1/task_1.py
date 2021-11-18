"""
In previous homework task 4, you wrote a cache function that remembers other
function output value.
Modify it to be a parametrized decorator, so that the following code::

    @cache(times=3)
    def some_function():
        pass


Would give out cached value up to `times` number only.
Example::

    @cache(times=2)
    def f():
        return input('? ')   # careful with input() in python2, use raw_input()
        instead

    ''>>> f()
    ? 1
    '1'
    ''>>> f()     # will remember previous value
    '1'
    ''>>> f()     # but use it up to two times only
    '1'
    ''>>> f()
    ? 2
    '2'

"""
from typing import Callable


def cache(times: int) -> Callable:
    """
    Remembers other function output value. Gives out cached value up to "times"
    number only.
    :param times: quantity of returned cached values.
    :return: Wrapper around recieved functon with cache functionality.
    """

    def cache_func(func: Callable) -> Callable:
        """
        Functtion accepts another function as an argument
        :param func: input function
        :return: such a function, so the every call to initial one should be
        cached
        """
        counter = 0
        cache_dict = {}

        def wrapper(*args):
            nonlocal counter, cache_dict

            if counter == times:
                cache_dict.pop(args, None)
                counter = 0

            if args not in cache_dict:
                cache_dict[args] = func(*args)
            else:
                counter += 1
            return cache_dict[args]

        return wrapper
    return cache_func
