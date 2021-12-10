"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of counter
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    """
    Function takes element and finds the number of counter of this element in
    the tree.
    Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
    :param tree: dictionary
    :param element: any basic structures
    (str, list, tuple, dict, set, int, bool)
    :return: integer, number of occurrences in the tree.
    """
    counter = 0
    if isinstance(tree, dict):
        tree = tree.values()

    for value in tree:
        if value == element:
            counter += 1
        if isinstance(value, (str, bool, int, set, tuple)):
            continue
        counter += find_occurrences(value, element)
    return counter
