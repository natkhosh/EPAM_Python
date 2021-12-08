"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""
from typing import List


def str_parser(string: str) -> List:
    """
    Function formats string into list of chars and removes backspace
    characters (#) and element before them.
    :param string: string
    :return: list of chars
    """
    list_of_chars = []
    for char in string:
        if char != '#':
            list_of_chars.append(char)
        else:
            if len(list_of_chars) > 0:
                list_of_chars.pop(-1)
    return list_of_chars


def backspace_compare(first: str, second: str) -> bool:
    """
    Function compares strings
    :param first: string
    :param second: string
    :return: if equal returns True, otherwise False
    """
    return True if str_parser(first) == str_parser(second) else False


print(backspace_compare("a#c", "b"))
