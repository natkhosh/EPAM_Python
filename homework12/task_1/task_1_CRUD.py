from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from homework12.task_1.task_1_models import (Homework, HomeworkResult, Student,
                                             Teacher)

DATABASE = 'sqlite:///main.db'


@contextmanager
def session_scope(database: str) -> Session:
    """
    Function provides a transactional scope around a series of operations:
    - database connection
    - session manipulations
    :param database: database path
    :return: session
    """

    engine = create_engine(database, echo=True)
    session = Session(bind=engine)

    try:
        yield session
        session.commit()

    except Exception as ex:
        session.rollback()
        print(ex)

    finally:
        session.close()


def main():
    """
    Function updates database with class instances.
    """
    objects = [
        Student(first_name='Roman', last_name='Petrov'),
        Student(first_name='Lev', last_name='Sokolov'),
        Teacher(first_name='Daniil', last_name='Shadrin'),
        Teacher(first_name='Aleksandr', last_name='Smetanin'),
        Homework(text='Learn OOP', deadline=1, author=1),
        Homework(text='Read docs', deadline=5, author=1),
        HomeworkResult(homework=1, solution='I have done this hw', author=1),
        HomeworkResult(homework=2, solution='I have done this hw too',
                       author=2)
    ]

    with session_scope(DATABASE) as session:
        session.add_all(objects)


if __name__ == "__main__":
    main()
