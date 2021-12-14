"""
Homework 2:
Preamble
We have a database file (example.sqlite) in sqlite3 format with some tables
and data. All tables have 'name' column and maybe some additional ones.

Data retrieval and modifications are done with sqlite3 module by issuing SQL
statements. For example, to get all data from TABLE1:

import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('SELECT * from TABLE1')
data = cursor.fetchall()   # will be a list with data.
instead of getting all data at once, you can use .fetchone() calls and named
expressions:

while row:=cursor.fetchone():
    print(row)
To get a row with specific name equal to some value:

import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('SELECT * from presidents where name=:name', {name:'Yeltsin'})
data = cursor.fetchall()  # will get all records with this name. You can also
use .fetchone() to get one record.
in order to get record with first name (sorted alphabetically) use SQL
expression SELECT * from presidents order by name asc limit 1 in order to get
record after specified (sorted alphabetically) use SQL expression
SELECT * from presidents where name > :name order by name limit. To get
amount of records in table TABLE1, use select count(*) from TABLE1 query.

Please refer to this documents for more information about how to retrieve
data from sqlite database:
DBAPI: https://www.python.org/dev/peps/pep-0249/
sqlite3 module: https://docs.python.org/3/library/sqlite3.html

Task
Write a wrapper class TableData for database table, that when initialized
with database name and table acts as collection object
(implements Collection protocol).
Assume all data has unique values in 'name' column. So, if
presidents = TableData(database_name='example.sqlite', table_name='presidents')

then
len(presidents) will give current amount of rows in presidents table in
database presidents['Yeltsin'] should return single data row for president
with name Yeltsin 'Yeltsin' in presidents should return if president with
same name exists in table object implements iteration protocol. i.e. you could
use it in for loops::
for president in presidents:
print(president['name'])
all above mentioned calls should reflect most recent data. If data in table
changed after you created collection instance, your calls should return
updated data.
Avoid reading entire table into memory. When iterating through records, start
reading the first record, then go to the next one, until records are exhausted.
When writing tests, it's not always neccessary to mock database calls
completely. Use supplied example.sqlite file as database fixture file
"""
import sqlite3
from typing import Tuple


class TableData:
    """
    Class initializes with database name and table as collection object
    (implements Collection protocol).
    """

    def __init__(self, database_name: str, table_name: str):
        """
        Method to initialize the object’s attributes
        :param database_name: string, database file
        :param table_name: string, table name
        """
        self.table_name = table_name
        self._conn = sqlite3.connect(database_name)
        self._conn.row_factory = sqlite3.Row
        self._cursor = self._conn.cursor()

    def __enter__(self):
        """
        Method make a database connection
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Method take sure the database connection gets closed.
        :param exc_type: indicates class of exception.
        :param exc_val: indicates type of exception .
        :param exc_tb: traceback is a report which has all of the information
        needed to solve the exception.
        """
        self._conn.cursor().close()
        self._conn.close()

    def __len__(self) -> int:
        """
        Method returns the length, the number of rows in a table.
        :return: int, the number of rows in a table
        """
        return self._conn.execute(
            f"SELECT COUNT(*) FROM {self.table_name}"
        ).fetchone()[0]

    def __getitem__(self, item) -> Tuple:
        """
        Method returns a single row from the table of a specific name
        :param item: str, key whose value should be returned
        :return: tuple, returns a single row from the table of a specific name
        """
        self._cursor.execute(
            f"SELECT * FROM {self.table_name} where name ='{item}'"
        )
        return tuple(self._cursor.fetchone())

    def __contains__(self, item) -> bool:
        """
        Method checks that table contains a specified name
        :param item: str, value whose should be checked
        :return: True if an entry with a specified name is present in table,
        otherwise False
        """
        self._cursor.execute(
            f"SELECT * FROM {self.table_name} where name ='{item}'"
        )
        return self._cursor.fetchone()

    def __iter__(self) -> Tuple:
        """
        Initializes an iterator protocol for the table.
        :return: tuple, contain rows of the table
        """
        yield from self._cursor.execute(f"SELECT * from {self.table_name}")


if __name__ == "__main__":
    with TableData(
        database_name="example.sqlite", table_name="presidents"
    ) as presidents:
        print(len(presidents))
        for president in presidents:
            print(president["country"])
        # print(presidents["Yeltsin"])
        # print("Yeltsin" in presidents)
        # print("Obama" in presidents)
