from typing import Any, List

import pytest

from homework3.task_3.task_3 import make_filter

sample_data = [
     {
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     }
]


@pytest.mark.parametrize(
    "kwargs, some_data, expected_result",
    [
        ({"name": "polly", "type": "bird"}, sample_data, [sample_data[1]]),
        ({"name": "Bill", "type": "person"}, sample_data, [sample_data[0]]),
        ({"name": "Kenny", "is_dead": True}, sample_data, []),

    ],
)
def test_make_filter(
    kwargs, some_data: List[Any], expected_result: List[Any]
):
    """
    Testing that function generate filter object for specified keywords.
    """
    assert make_filter(**kwargs).apply(some_data) == expected_result
