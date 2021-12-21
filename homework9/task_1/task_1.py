"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from itertools import chain
from pathlib import Path
from typing import Iterator, List, Union


def gen_from_file(file: str) -> Iterator:
    """
    Function opens file and transforms content in integer.
    :param file: string, path to file
    :return: generator of integers
    """
    with open(file, "r", encoding='utf-8') as fi:
        yield from [int(line) for line in fi]


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    """
    Function sorted merges integer from files and returns generator.
    :param file_list: list of paths to files
    :return: generator of sorted integers
    """
    files_values = [gen_from_file(file) for file in file_list]

    yield from sorted(chain(*files_values))


if __name__ == "__main__":

    print(list(merge_sorted_files(['file1.txt', 'file2.txt', 'file3.txt'])))
