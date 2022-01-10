"""
- (*) optional task: write standalone script (get_report.py) that
    retrieves and stores the following information into CSV file report.csv

        for all done (completed) homeworks:
            - Student name (who completed homework)
            - Creation date
            -Teacher name who created homework
"""
import csv

from homework12.task_1.task_1_CRUD import session_scope
from homework12.task_1.task_1_models import (Homework, HomeworkResult, Student,
                                             Teacher)

DATABASE = 'sqlite:///main.db'


with session_scope(DATABASE) as session:

    query = session.query(HomeworkResult, Homework, Student, Teacher)
    query = query.join(HomeworkResult, HomeworkResult.homework == Homework.id)
    query = query.join(Student, Student.id == HomeworkResult.author)
    query = query.join(Teacher, Teacher.id == Homework.author)
    records = query.all()

    with open("report.csv", "w") as report:
        writer = csv.writer(report)
        for _, homework, student, teacher in records:
            data = [student.first_name, homework.created, teacher.first_name]
            writer.writerow(data)
