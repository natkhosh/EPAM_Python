from datetime import timedelta
from typing import NamedTuple

import pytest

from homework6.task_2.task_2 import (DeadlineError, Homework, HomeworkResult,
                                     Student, Teacher)


class TestData(NamedTuple):
    """
    A utility class for creating test data structure
    """
    opp_teacher: Teacher
    advanced_python_teacher: Teacher
    lazy_student: Student
    good_student: Student
    oop_hw: Homework
    docs_hw: Homework
    result_1: HomeworkResult
    result_2: HomeworkResult
    result_3: HomeworkResult
    expired_homework: Homework


@pytest.fixture
def test_data():
    """
    Creating class instances for running the tests
    """
    opp_teacher = Teacher('Shadrin', 'Daniil')
    advanced_python_teacher = Teacher('Smetanin', 'Aleksandr')
    lazy_student = Student('Petrov', 'Roman')
    good_student = Student('Sokolov', 'Lev')
    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)
    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    expired_homework = advanced_python_teacher.create_homework(
        'Learn functions', -1)

    return TestData(opp_teacher,
                    advanced_python_teacher,
                    lazy_student,
                    good_student,
                    oop_hw,
                    docs_hw,
                    result_1,
                    result_2,
                    result_3,
                    expired_homework)


def test_teacher_attributes(test_data):
    """
    Testing that the attributes of a class Teacher are correct
    """
    assert test_data.opp_teacher.last_name == 'Shadrin'
    assert test_data.opp_teacher.first_name == 'Daniil'
    assert test_data.advanced_python_teacher.last_name == 'Smetanin'
    assert test_data.advanced_python_teacher.first_name == 'Aleksandr'


def test_student_attributes(test_data):
    """
    Testing that the attributes of a class Student are correct
    """
    assert test_data.lazy_student.last_name == 'Petrov'
    assert test_data.lazy_student.first_name == 'Roman'
    assert test_data.good_student.last_name == 'Sokolov'
    assert test_data.good_student.first_name == 'Lev'


def test_teacher_create_homework(test_data):
    """Testing that the attributes of created homework are correct"""
    assert test_data.oop_hw.text == 'Learn OOP'
    assert test_data.oop_hw.deadline == timedelta(1)
    assert test_data.docs_hw.text == 'Read docs'
    assert test_data.docs_hw.deadline == timedelta(5)


def test_teacher_check_homework_method_positive(test_data):
    """Testing that if text of answer is longer than 5
    symbols and doesn't duplicate others, returns True and an instance
    HomeworkResult add to homework_done. """
    assert test_data.opp_teacher.check_homework(test_data.result_1) is True
    assert test_data.oop_hw in test_data.opp_teacher.homework_done


def test_teacher_check_homework_method_negative(test_data):
    """Testing that function returns False and doesn't add
    an instance HomeworkResult to homework_done' when text of answer has less
    than 5 symbols"""
    assert test_data.opp_teacher.check_homework(test_data.result_3) is False
    assert test_data.docs_hw not in test_data.opp_teacher.homework_done


def test_teacher_reset_results_global(test_data):
    """Testing that function resets results of all homeworks."""
    test_data.opp_teacher.reset_results()
    assert len(test_data.opp_teacher.homework_done) == 0


def test_teacher_reset_results_hw(test_data):
    """ Testing that function resets results of current homework."""
    test_data.opp_teacher.check_homework(test_data.result_1)
    test_data.opp_teacher.check_homework(test_data.result_2)
    test_data.opp_teacher.reset_results(test_data.oop_hw)
    assert test_data.oop_hw not in test_data.opp_teacher.homework_done


def test_teacher_homework_done_class_attribute(test_data):
    """Testing that 'homework_done' is a class attribute
    that is shared by all instances of a Teacher class"""
    test_data.opp_teacher.check_homework(test_data.result_1)
    temp_1 = test_data.opp_teacher.homework_done
    test_data.advanced_python_teacher.check_homework(test_data.result_2)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2


def test_student_homework_deadline_exception(test_data):
    """Testing that DeadlineError with a message 'You are late' is raised if
    deadline of the homework has expired"""
    with pytest.raises(DeadlineError, match='You are late'):
        test_data.lazy_student.do_homework(test_data.expired_homework, 'done')


# def test_student_homework_result_wrong_object_exception(test_data):
#     """Testing that TypeError with a message 'You gave not a Homework object'
#     is raised if homework parameter is not an instance of a class Homework"""
#     with pytest.raises(TypeError, match='You gave a not Homework object'):
#        HomeworkResult(test_data.good_student, "fff", "Solution")
