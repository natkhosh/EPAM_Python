"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """
    Function finds the most common and the least common elements.
    he most common element is the element that appears more than n // 2 times.
    The least common element is the element that appears fewer than other.
    :param inp: list jf elements
    :return: tuple with the most common and the least common elements
    """
    counter: dict = {}
    for item in inp:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

    items_list = sorted(counter, key=lambda key_: counter[key_])

    return items_list[-1], items_list[0]
