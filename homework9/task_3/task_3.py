"""
Write a function that takes directory path, a file extension and an optional
tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
>> universal_file_counter(test_dir, "txt")
6
>> universal_file_counter(test_dir, "txt", str.split)
6
"""
from pathlib import Path, PureWindowsPath
from typing import Callable, Optional, Union


def universal_file_counter(
        dir_path: Union[str, Path], file_extension: str,
        tokenizer: Optional[Callable] = None) -> int:
    """
    This function counts lines in all files with file extension and an optional
    tokenizer, if there is no tokenizer. And if the tokenizer, it will count
    tokens.
    :param dir_path: path to directory
    :param file_extension: extension of files
    :param tokenizer: string method
    :return: integer, count of lines or tokens
    """
    count = 0
    path = Path(dir_path)

    if not path.is_dir():
        raise OSError('Directory not found')

    files_list = path.glob(f'*{file_extension}')

    for fn in files_list:
        with open(PureWindowsPath(path).joinpath(fn), "r") as f:
            for line in f:
                if tokenizer:
                    count += len(tokenizer(line))
                else:
                    count += 1
    return count


if __name__ == "__main__":
    print(universal_file_counter('../tests', ".txt"))
    print(universal_file_counter('../tests', ".txt", str.split))
