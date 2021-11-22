import os

import pytest

from homework4.task_1.task_1 import read_magic_number


@pytest.fixture()
def file_generator(file_pass, value):
    with open(file_pass, "w") as fi:
        fi.write(value)
    yield file_pass
    os.remove(file_pass)


@pytest.mark.parametrize(
    "file_pass, value",
    [
        ("data.txt", "1"),
        ("data1.txt", "2.534"),
        ("data2.txt", "1\n"),
    ],
)
def test_read_magic_number_positive(file_pass, value, file_generator):
    """Testing that function returns True within a given range"""
    assert read_magic_number(file_generator) is True


@pytest.mark.parametrize(
    "file_pass, value",
    [
        ("data.txt", "-3"),
        ("data1.txt", "0"),
        ("data2.txt", "3.2\n"),
    ],
)
def test_read_magic_number_negative(file_pass, value, file_generator):
    """Testing that function returns False with a number that is out of
    a given range"""
    assert read_magic_number(file_generator) is False


@pytest.mark.parametrize(
    "file_pass, value",
    [
        ("data.txt", "some data"),
        ("data1.txt", ""),
        ("data2.txt", "22я"),
    ],
)
def test_read_magic_number_value_error(file_pass, value, file_generator):
    """Testing that ValueError is raised if the data on the first line in
    the file is not a number"""
    with pytest.raises(ValueError):
        read_magic_number(file_generator)


def test_read_file_exceptions():
    """Testing that FileNotFoundError exception is raised if a file does
    not exist"""
    with pytest.raises(FileNotFoundError):
        read_magic_number("no_file.txt")
