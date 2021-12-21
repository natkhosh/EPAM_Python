import pytest

from homework9.task_2.task_2 import Supressor, supressor


@pytest.mark.parametrize(
    "exception",
    [(IndexError,), (ValueError,)]
)
def test_class_supressor(exception):
    """
    Testing that context manager suppresses passed exception.
    """
    assert Supressor(exception)


@pytest.mark.parametrize(
    "exception",
    [(IndexError,), (ValueError,), (KeyError,)]
)
def test_generator_supressor(exception):
    """
    Testing that context manager suppresses passed exception.
    """
    assert supressor(exception)
