import pytest

from homework7.task_2.task_2 import backspace_compare


@pytest.mark.parametrize('value_first, value_second, expected_result',
                         [
                             ("ab#c", "ad#c", True),
                             ("a##c", "#a#c", True)
                         ])
def test_backspace_compare_positive(value_first, value_second,
                                    expected_result):
    """ Testing that function compares the strings are equal """
    assert backspace_compare(value_first, value_second) == expected_result


@pytest.mark.parametrize('value_first, value_second, expected_result',
                         [
                             ("a#c", "b", False),
                             ("c#", "#c", False)
                         ])
def test_backspace_compare_negative(value_first, value_second,
                                    expected_result):
    """ Testing that function compares the strings are not equal """
    assert backspace_compare(value_first, value_second) == expected_result
