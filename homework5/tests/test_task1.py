from datetime import timedelta
from typing import NamedTuple

import pytest

from homework5.task_1.task_1 import Homework, Student, Teacher


class TestData(NamedTuple):
    teacher: Teacher
    student: Student
    expired_homework: Homework
    oop_homework: Homework


@pytest.fixture
def test_data():
    """Creating class instances for running the tests"""
    teacher = Teacher('Shadrin', 'Daniil')
    student = Student('Petrov', 'Roman')
    expired_homework = teacher.create_homework('Learn functions', 0)
    oop_homework = teacher.create_homework('create 2 simple classes', 5)
    return TestData(teacher, student, expired_homework, oop_homework)


def test_teacher_attributes(test_data):
    """Testing that the attributes of a class Teacher are correct"""
    assert test_data.teacher.last_name == 'Shadrin'
    assert test_data.teacher.first_name == 'Daniil'


def test_student_attributes(test_data):
    """Testing that the attributes of a class Student are correct"""
    assert test_data.student.last_name == 'Petrov'
    assert test_data.student.first_name == 'Roman'


def test_homework_attributes(test_data):
    """Testing that the attributes of a class Homework are correct"""
    assert test_data.expired_homework.deadline == timedelta(0)
    assert test_data.expired_homework.text == 'Learn functions'


def test_student_do_homework_method_expired(test_data, capsys):
    """Testing that class Student method 'do_homework' returns a correct result
    with an expired instance of a Homework class"""
    test_data.student.do_homework(test_data.expired_homework)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'You are late'
