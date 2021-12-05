"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime

1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean

2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None

3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
from datetime import datetime, timedelta
from typing import Union


class Homework:
    """
    A class describes an instance of homework.
    Create Homework tasks, based on text and deadline.
    Attributes:
        text: text of the current homework
        deadline: number of days to complete the assignment current homework
                (datetime.timedelta object)
        created: the date and time of the instance's creation.
    """

    def __init__(self, text: str, deadline: int):
        """
        Constructor method
        """
        self.text = text
        self.deadline = timedelta(days=deadline)
        self.created = datetime.now()

    def is_active(self) -> bool:
        """
        Checks is there time till deadline of the current homework.
        :return:  if the deadline has not expired return True, otherwise False
        """
        return True if datetime.now() - self.created < self.deadline else False


class Student:
    """
    A class describes an instance of a student.
    Attributes:
        first_name: the name of a student
        last_name: the surname of a student
    """

    def __init__(self, last_name, first_name):
        """
        Constructor method
        """
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(homework: Homework) -> Union[Homework, None]:
        """
        Function checks is the deadline of the given homework expired or not.
        :param homework: an instance of the Homework class that a student is
        going to do.
        :return: if deadline hasn't expired return the received instance
        of the Homework class, otherwise prints "You are late" and returns None
        """
        if not homework.is_active():
            print('You are late')
            return
        return homework


class Teacher:
    """
    A class describes an instance of a student.
    Attributes:
        first_name: the name of a teacher
        last_name: the surname of a teacher
    """

    def __init__(self, last_name, first_name):
        """
        Constructor method
        """
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(text: str, deadline: int) -> Homework:
        """
        Creates an instance of the Homework class.
        :param text: text of created homework
        :param deadline: int: the number of days to complete this homework
        :return: an instance of Homework class
        """
        return Homework(text, deadline)
