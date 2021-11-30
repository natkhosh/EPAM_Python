import pytest

from homework5.task_2.task_2 import custom_sum


def test_save_info():
    """
    Testing that decorator saves the docstring and the name from an original
    function
    """
    assert custom_sum.__doc__ == "This function can sum any objects which " \
                                 "have __add___"
    assert custom_sum.__name__ == 'custom_sum'


@pytest.mark.parametrize('value, expected_result',
                         [
                             (([1, 2, 3], [4, 5]), [1, 2, 3, 4, 5]),
                             ((1, 2, 3, 4), 10)
                         ])
def test_save_original_func(value, expected_result):
    """
    Testing that original function is saved as well
    """
    without_print = custom_sum.__original_func

    assert custom_sum(*value) == expected_result
    assert without_print(*value) == expected_result
