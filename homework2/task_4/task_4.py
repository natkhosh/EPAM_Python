"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.

def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable


def cache(func: Callable) -> Callable:
    """
    Functtion accepts another function as an argument
    :param func: input function
    :return: such a function, so the every call to initial one should be cached
    """
    cache_dict = {}

    def mem_func(*args):
        if args in cache_dict:
            return cache_dict[args]
        else:
            cache_dict[args] = func(*args)
            return cache_dict[args]

    return mem_func
