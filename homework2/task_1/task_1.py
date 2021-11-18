"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from collections import Counter
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    Function reads file and finds 10 longest words consisting from largest
    amount of unique symbols
    :param file_path: path to file
    :return: list of 10 longest words
    """
    with open(file_path, "r", encoding="unicode-escape") as fi:
        s = ""
        words_counter = {}
        for i in fi:
            s += i
        words = s.replace("-\n", "").split()

        for word in words:
            word = word.strip("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
            if word not in words_counter:
                words_counter[word] = len(set(word))

    return sorted(
        words_counter,
        key=lambda dict_key: words_counter[dict_key],
        reverse=True
    )[:10]


def get_rarest_char(file_path: str) -> str:
    """
    Function reads file and finds rarest symbol for document.
    :param file_path: path to file
    :return: str: rarest symbol for document
    """
    symbols_counter = {}
    with open(file_path, encoding="unicode-escape") as file:
        for line in file:
            for symbol in line:
                if symbol not in symbols_counter:
                    symbols_counter[symbol] = 1
                else:
                    symbols_counter[symbol] += 1

    min_dict_key = min(symbols_counter, key=symbols_counter.get)
    rarest_chars = [
        k for (k, v) in symbols_counter.items()
        if v == symbols_counter[min_dict_key]
    ]

    return "".join(rarest_chars)


def count_punctuation_chars(file_path: str) -> int:
    """
    Function reads file and count every punctuation char.
    :param file_path: path to file
    :return: integer amount punctuation char
    """
    punctuation_chars = string.punctuation + "—"
    amount = 0
    with open(file_path, encoding="unicode-escape") as file:
        for line in file:
            for symbol in line:
                if symbol in punctuation_chars:
                    amount += 1
    return amount


def count_non_ascii_chars(file_path: str) -> int:
    """
    Function reads file and count every non ascii char.
    :param file_path: path to file
    :return: integer amount non ascii char
    """
    amount = 0
    with open(file_path, encoding="unicode-escape") as file:
        for line in file:
            for symbol in line:
                if not symbol.isascii():
                    amount += 1
    return amount


def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    Function reads file and finds most common non ascii char for document.
    :param file_path: path to file
    :return: str: most common non ascii char for document
    """
    symbols_counter = Counter()
    with open(file_path, encoding="unicode-escape") as file:
        for line in file:
            for symbol in line:
                if not symbol.isascii():
                    if symbol not in symbols_counter:
                        symbols_counter[symbol] = 1
                    else:
                        symbols_counter[symbol] += 1
    return symbols_counter.most_common(1)[0][0]
