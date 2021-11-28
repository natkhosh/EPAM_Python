from unittest.mock import patch

import pytest

from homework4.task_2.task2 import count_dots_on_i


@pytest.mark.parametrize("value, url, expected_result",
                         [('Testing with Python', "https://example.com/", 2),
                          ("<p>Hello world!<p>", "https://example.com/", 0), ])
def test_count_dots_on_i_positive(value: str, url: str, expected_result: int):
    """Testing that function returns a correct result with a sample data
     from mock object"""
    with patch('requests.get') as mock_request:
        mock_request.return_value.text = value
        assert count_dots_on_i(url) == expected_result


@pytest.mark.parametrize("url, expected_result",
                         [("https://example.com/", 59)])
def test_count_dots_on_i_positive_not_mocked(url: str, expected_result: int):
    """Testing that function returns a correct result"""
    assert count_dots_on_i(url) == expected_result


def test_count_dots_on_i_exception():
    """Testing that ValueError is raised in case of any network error"""
    with patch('requests.get') as mock_request:
        url = "https://example112121111.com/"
        mock_request.side_effect = ValueError
        with pytest.raises(ValueError):
            count_dots_on_i(url)
