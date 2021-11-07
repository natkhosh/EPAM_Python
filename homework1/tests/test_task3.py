import os
from typing import Tuple

import pytest

from homework1.task_3.task_3 import find_maximum_and_minimum


@pytest.mark.parametrize(
    "value, expected_result",
    [("../task_3/some_file.txt", (-1, 78)), ("../task_3/some_file1.txt", (0, 123123))],
)
def test_find_maximum_and_minimum(value: str, expected_result: Tuple[int, int]):
    """
    Testing that function finds max and min number correctly
    """
    cur_path = os.path.dirname(__file__)
    assert find_maximum_and_minimum(os.path.join(cur_path, value)) == expected_result
