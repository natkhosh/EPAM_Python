from typing import Union

import pytest

from homework8.task_1.task_1 import KeyValueStorage

storage = KeyValueStorage('../task_1/task_1.txt')


def test_KeyValueStorage_positive():
    """Testing that the attributes of a class KeyValueStorage has keys and
    values accessible as collection items and as attributes"""
    assert storage.name == 'kek'
    assert storage['last_name'] == 'top'
    assert storage.power == 9001


@pytest.mark.parametrize("value, expected_result", [('power', 9001)])
def test_KeyValueStorage_check_int(value: str,
                                   expected_result: Union[int, str]):
    """Testing that if a value can be treated both as a number and a string,
    it is treated as number """

    assert isinstance(storage.value, int)


def test_KeyValueStorage_error():
    """Testing that ValueError is raised if value cannot be assigned to an
    attribute"""
    with pytest.raises(ValueError):
        assert KeyValueStorage('task_2.txt')
