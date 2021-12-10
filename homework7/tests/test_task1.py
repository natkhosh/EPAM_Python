import pytest

from homework7.task_1.task_1 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}


@pytest.mark.parametrize('element, expected_result',
                         [
                             ("RED", 6),
                             ("list", 1),
                             ("GREEN", 0),
                             (["RED", "BLUE"], 1),
                             ({"nested_key": "RED"}, 1),
                         ],)
def test_find_occurrences(element, expected_result):
    """ Testing that function finds the number of counter of element in
    the tree"""
    assert find_occurrences(example_tree, element) == expected_result
