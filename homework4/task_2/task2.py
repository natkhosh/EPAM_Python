"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.

Write a test that check that your function works.
Test should use Mock instead of real network interactions.

You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - test could be run without internet connection

You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests


\\>>> count_dots_on_i("https://example.com/")
59

* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""

import requests


def count_dots_on_i(url: str) -> int:
    """
    Function accepts an URL as input and count how many letters `i` are
    present in the HTML by this URL.
    :param url: address of web-page on the Internet
    :return: amount of letters "i" are present in the HTML by this URL
    """
    response = requests.get(url).text
    try:
        count = 0
        for i in response:
            if i == 'i':
                count += 1

        return count
    except requests.exceptions.RequestException:
        raise ValueError
