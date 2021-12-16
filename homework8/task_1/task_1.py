"""
Homework 1:
We have a file that works as key-value storage, each line is represented as key
and value separated by = symbol, example:

name=kek last_name=top song_name=shadilay power=9001

Values can be strings or integer numbers. If a value can be treated both as a
number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt') that has its keys and values
accessible as collection items and as attributes. Example: storage['name']
# will be string 'kek' storage.song_name # will be 'shadilay' storage.power
# will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute (for example when
there's a line 1=something) ValueError should be raised. File size is expected
to be small, you are permitted to read it entirely into memory.
"""
from collections import defaultdict
from typing import Union


class KeyValueStorage:
    """ Class for saving attributes from a file. """

    def __init__(self, path: str):
        """
        Method to initialize the object’s attributes
        :param path: path to file which is a key-value storage file.
        """
        self._file_dict = defaultdict(int)
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                key, value = line.strip().split('=')
                if key.isdigit():
                    raise ValueError('The key should be a string')
                if value.isnumeric():
                    value = int(value)

                self._file_dict[key] = value

    def __getattr__(self, key: str) -> Union[str, int]:
        """
        Get value whose key accessible as attribute.
        :param key: key whose value should be returned
        :return: value defined for the key
        """
        return self._file_dict[key]

    def __getitem__(self, key: str) -> Union[str, int]:
        """
        Get value whose key accessible as collection item.
        :param key: key whose value should be returned
        :return: value defined for the key
        """
        return self._file_dict[key]
