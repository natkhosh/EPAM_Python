import pytest

from homework8.task_2.task_2 import TableData

database_name = '../task_2/example.sqlite'
table_name = "presidents"


@pytest.fixture()
def cm_presidents():
    """
    Context manager that create a SQLite database connection and close it
    when it's done.
    """
    with TableData(database_name, table_name) as presidents:
        yield presidents


def test_check_table_len(cm_presidents):
    """
    Testing that method __len__ returns a correct length of
    specified tables from database.
    """
    assert len(cm_presidents) == 3


@pytest.mark.parametrize('value, expected_result',
                         [("Yeltsin", ("Yeltsin", 999, "Russia"))])
def test_check_getitem(value: str, expected_result: tuple, cm_presidents):
    """
    Testing that method __getitem__ returns correct entries from the tables
    with specified values.
    """
    assert cm_presidents[value] == expected_result


def test_check_table_contain(cm_presidents):
    """
    Testing that method __contains__ resurns a correct result when entries
    with specified values are present in the tables.
    """
    assert "Yeltsin" in cm_presidents
    assert "Trump" in cm_presidents
    assert "Putin" not in cm_presidents


def test_check_iterator(cm_presidents):
    """
    Testing that method __iter__ works correctly and it's possible to use
    tables as iterable.
    """
    country = [president["country"] for president in cm_presidents]
    assert country == ['Russia', 'US', 'Kekistan']
