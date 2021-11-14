from typing import List, Sequence

import pytest

from homework2.task_1.task_1 import *


@pytest.mark.parametrize(
    "file_path, expected_result",
    [
        (
            "homework2/task_1/data.txt",
            [
                "Souveränitätsansprüche",
                "unmißverständliche",
                "Bevölkerungsabschub",
                "symbolischsakramentale",
                "Kollektivschuldiger",
                "unverhältnismäßig",
                "Werkstättenlandschaft",
                "Schicksalsfiguren",
                "politisch-strategischen",
                "Selbstverständlich",
            ],
        ),
        (
            "homework2/task_1/ data1.txt",
            [
                "vorgebahnte",
                "Betrachtung",
                "hinausführen",
                "bedenklichen",
                "verbirgt",
                "vielmehr",
                "Waldgang",
                "hinter",
                "Ausflug",
                "gefaßt",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(file_path: str, expected_result: List[str]):
    """
    Testing that function actual finds 10 longest words consisting from largest amount of unique symbols.
    """
    assert get_longest_diverse_words(file_path) == expected_result
