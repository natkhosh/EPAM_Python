"""
Using ORM framework of your choice, create models classes created in Homework 6
(Teachers, Students, Homework and others). - Target database should be sqlite
(filename main.db localted in current directory) - ORM framework should
support migrations.

Utilizing that framework capabilities, create:
    - a migration file, creating all necessary database structures.
    - a migration file (separate) creating at least one record in each created
    database table
    - (*) optional task: write standalone script (get_report.py) that
    retrieves and stores the following information into CSV file report.csv

        for all done (completed) homeworks:
            Student name (who completed homework) Creation date Teacher name
            who created homework

Utilize ORM capabilities as much as possible, avoiding executing raw SQL
queries.
"""
from datetime import datetime

from sqlalchemy import (Column, DateTime, ForeignKey, Integer, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base

DATABASE = 'sqlite:///main.db'
Base = declarative_base()


class Homework(Base):
    __tablename__ = 'homeworks'
    id = Column(Integer, primary_key=True)
    text = Column(String(100), nullable=False)
    deadline = Column(Integer, nullable=False)
    created = Column(DateTime(), default=datetime.now)

    def __str__(self) -> str:
        return self.text


class HomeworkResult(Base):
    __tablename__ = 'homeworkresults'
    homework = Column(None, ForeignKey('homeworks.id'), primary_key=True)
    solution = Column(String(100), nullable=False)
    author = Column(None, ForeignKey('students.id'))
    created = Column(DateTime(), default=datetime.now)

    def __str__(self) -> str:
        return self.solution


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    # def __repr__(self):
    #     return "<Student(first_name='%s', last_name='%s', id='%s')>" % (
    #         self.first_name, self.last_name, self.id)


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


def main():
    engine = create_engine(DATABASE, echo=True)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
