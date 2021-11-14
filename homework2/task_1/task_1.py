"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    Function reads file and finds 10 longest words consisting from largest amount of unique symbols
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
        words_counter, key=lambda dict_key: words_counter[dict_key], reverse=True
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
    return min(symbols_counter, key=lambda dict_key: symbols_counter[dict_key])


def count_punctuation_chars(file_path: str) -> int:
    """
    Function reads file and count every punctuation char.
    :param file_path: path to file
    :return: integer amount punctuation char
    """
    punctuation_chars = "!\"#$%&'()*+,—-./:;<=>?@[\\]^_`{|}~"
    amount = 0
    with open(file_path, encoding="unicode-escape") as file:
        # print(file.read())
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
                    # print(symbol)
                    amount += 1
    return amount


def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    Function reads file and finds most common non ascii char for document.
    :param file_path: path to file
    :return: str: most common non ascii char for document
    """
    symbols_counter = {}
    with open(file_path, encoding="unicode-escape") as file:
        for line in file:
            for symbol in line:
                if not symbol.isascii():
                    if symbol not in symbols_counter:
                        symbols_counter[symbol] = 1
                    else:
                        symbols_counter[symbol] += 1
    return max(symbols_counter, key=lambda dict_key: symbols_counter[dict_key])


# print(get_most_common_non_ascii_char("../task_1/data.txt"))


# 1.2 Список всех самых редких символ для документа
# sorted_tuples = sorted(symbols_counter.items(), key=lambda item: item[1])
# print(sorted_tuples)
# r = []
# for k, v in symbols_counter.items():
#     if v == 1:
#         r.append(k)
# q = ''.join(r)
