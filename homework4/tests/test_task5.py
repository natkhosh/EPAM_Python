import pytest

from homework4.task_5.task_5 import fizzbuzz


@pytest.mark.parametrize("number, expected_result", [
    (5, ['1', '2', 'fizz', '4', 'buzz']),
    (7, ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7'])
])
def test_fizzbuzz_positive(number: int, expected_result: list):
    """Testing that function returns a generator of N FizzBuzz numbers"""
    assert list(fizzbuzz(number)) == expected_result


@pytest.mark.parametrize("number", [0, 1.5])
def test_fizzbuzz_negative(number: int):
    """Testing that ValueError exception is raised if a n not an integer and
    less than 1"""
    with pytest.raises(ValueError):
        list(fizzbuzz(number))
