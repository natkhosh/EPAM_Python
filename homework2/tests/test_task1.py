from typing import List

import pytest

from homework2.task_1.task_1 import (count_non_ascii_chars,
                                     count_punctuation_chars,
                                     get_longest_diverse_words,
                                     get_most_common_non_ascii_char,
                                     get_rarest_char)


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
            "homework2/task_1/data1.txt",
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
    Testing that function actual finds 10 longest words consisting from
    largest amount of unique symbols.
    """
    assert get_longest_diverse_words(file_path) == expected_result


@pytest.mark.parametrize(
    "file_path, expected_result",
    [
        ("homework2/task_1/data.txt", "›‹Yî’X()"),
        ("homework2/task_1/data1.txt", "W—IyTLAPGzBw"),
    ],
)
def test_get_rarest_char(file_path: str, expected_result: str):
    """
    Testing that function actual finds 10 longest words consisting from
    largest amount of unique symbols.
    """
    assert get_rarest_char(file_path) == expected_result


@pytest.mark.parametrize(
    "file_path, expected_result",
    [("homework2/task_1/data.txt", 5386), ("homework2/task_1/data1.txt", 8)],
)
def test_count_punctuation_chars(file_path: str, expected_result: int):
    """
    Testing that function actual count every punctuation char.
    """
    assert count_punctuation_chars(file_path) == expected_result


@pytest.mark.parametrize(
    "file_path, expected_result",
    [("homework2/task_1/data.txt", 2972), ("homework2/task_1/data1.txt", 6)],
)
def test_count_non_ascii_chars(file_path: str, expected_result: int):
    """
    Testing that function actual count every non ascii char.
    """
    assert count_non_ascii_chars(file_path) == expected_result


@pytest.mark.parametrize(
    "file_path, expected_result",
    [("homework2/task_1/data.txt", "ä"), ("homework2/task_1/data1.txt", "ü")],
)
def test_get_most_common_non_ascii_char(file_path: str, expected_result: str):
    """
    Testing that function actual count most common non ascii char for document.
    """
    assert get_most_common_non_ascii_char(file_path) == expected_result
