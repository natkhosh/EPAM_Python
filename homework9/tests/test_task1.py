from typing import List, Union

import pytest

from homework9.task_1.task_1 import merge_sorted_files


@pytest.mark.parametrize(
    'files_list, expected_result', [
        (['file1.txt', 'file2.txt', 'file3.txt'], [0, 1, 2, 3, 4, 5, 6, 8, 9]),
        (['file2.txt', 'file3.txt'], [0, 2, 4, 6, 8, 9])
    ]
)
def test_merge_sorted_files(files_list: List[Union[str, str]],
                            expected_result: List):
    """
     Testing that function sorted files and returns an iterator.
    """
    assert list(merge_sorted_files(files_list)) == expected_result


def test_merge_sorted_file_exception():
    """
    Testing that FileNotFoundError exception is raised if a file does
    not exist.
    """
    files_list = ['file11.txt', 'file2.txt', 'file3.txt']
    with pytest.raises(FileNotFoundError):
        raise list(merge_sorted_files(files_list))
