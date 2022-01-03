from datetime import datetime

from sqlalchemy import (Column, DateTime, ForeignKey, Integer, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///main.db', echo=True)
Base = declarative_base()


# class Person(Base):
#     __tablename__ = 'persons'
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String(50), nullable=False)
#     last_name = Column(String(50), nullable=False)

class Homework(Base):
    __tablename__ = 'homeworks'
    id = Column(Integer, primary_key=True)
    text = Column(String(100), nullable=False)
    deadline = Column(Integer, nullable=False)
    created = Column(DateTime(), default=datetime.now)


class HomeworkResult(Base):
    __tablename__ = 'homeworkresults'
    homework = Column(None, ForeignKey('homeworks.id'), primary_key=True)
    solution = Column(String(100), nullable=False)
    author = Column(None, ForeignKey('students.id'))
    created = Column(DateTime(), default=datetime.now)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Student(first_name='%s', last_name='%s', id='%s')>" % (
            self.first_name, self.last_name, self.id)


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
