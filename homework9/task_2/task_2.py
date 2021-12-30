"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>> with supressor(IndexError):
...    [][2]
"""
from contextlib import contextmanager


class Supressor:
    """
    Сontext manager, that suppresses passed exception.
    """

    def __init__(self, exception):
        """
        Method to initialize the object’s attributes
        :param exception:  any exception
        """
        self.exception = exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.exception is exc_type


@contextmanager
def supressor(exception):
    """
    Сontext manager, that suppresses passed exception.
    :param exception:  any exception
    """
    try:
        yield
    except exception:
        pass


if __name__ == "__main__":
    # with Supressor(IndexError):
    #     [][2]

    with supressor(IndexError):
        [][2]
