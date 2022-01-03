from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from homework12.task_1.task_1 import Homework, HomeworkResult, Student, Teacher

engine = create_engine('sqlite:///main.db', echo=True)
session = Session(bind=engine)

t1 = Teacher(first_name='Daniil', last_name='Shadrin')
t2 = Teacher(first_name='Aleksandr', last_name='Smetanin')

s1 = Student(first_name='Roman', last_name='Petrov')
s2 = Student(first_name='Lev', last_name='Sokolov')

h1 = Homework(text='Learn OOP', deadline=1)
h2 = Homework(text='Read docs', deadline=5)

hr1 = HomeworkResult(homework=1, solution='I have done this hw', author=1)
hr2 = HomeworkResult(homework=2, solution='I have done this hw too', author=2)


# if __name__ == '__main__':
# session.add_all([t1, t2, s1, s2, h1, h2])
# session.add(hr1)
# session.add(hr2)
#
#
# session.commit()
s = session.query(Student).first()
print(s)

# for i in s:
#     print(s.__dict__)
