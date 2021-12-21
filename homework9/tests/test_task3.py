from pathlib import Path
from typing import Callable, Optional, Union

import pytest

from homework9.task_3.task_3 import universal_file_counter


@pytest.mark.parametrize('dir_path, file_extension, tokenizer, '
                         'expected_result',
                         [
                             ('../tests', ".txt", None, 11),
                             ('../tests', ".txt", str.split, 13)
                         ])
def test_universal_file_counter(
        dir_path: Union[str, Path], file_extension: str,
        tokenizer: Optional[Callable], expected_result: int):
    """
    Testing that function counts lines in all files in directory with
    file extension and an optional tokenizer.
    """
    assert universal_file_counter(dir_path, file_extension,
                                  tokenizer) == expected_result


@pytest.mark.parametrize('dir_path, file_extension, tokenizer',
                         [
                             ('../test', ".txt", None),
                             ('../test', ".txt", str.split)
                         ])
def test_universal_file_counter_exception(
        dir_path: Union[str, Path], file_extension: str,
        tokenizer: Optional[Callable]):
    """
    Testing that OSError exception is raised if a directory does
    not exist.
    """
    with pytest.raises(OSError):
        raise universal_file_counter(dir_path, file_extension, tokenizer)
