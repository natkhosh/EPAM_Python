"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на #defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
from collections import defaultdict
from datetime import datetime, timedelta


class DeadlineError(Exception):
    """ Exception for timeout homework deadline """
    pass


class Person:
    """
    A class to represent a person
    Attributes:
        first_name: the name of a person
        last_name: the surname of a person
    """

    def __init__(self, last_name: str, first_name: str):
        """
        Method to initialize the object’s attributes
        """
        self.last_name = last_name
        self.first_name = first_name


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
        Method to initialize the object’s attributes
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


class HomeworkResult:
    """
    A class to represent the result of homework
    """

    def __init__(self, author, homework: Homework, solution: str):
        """
        Method to initialize the object’s attributes
        """
        if not isinstance(homework, Homework):
            raise TypeError('You gave a not Homework object')

        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.now()


class Student(Person):
    """
    A class describes an instance of a student, inherited class Person.
    """

    def __init__(self, *args):
        """
        Method to initialize the object’s attributes
        """
        super().__init__(*args)

    def do_homework(self, homework: Homework, result: str) -> HomeworkResult:
        """
        Function checks is the deadline of the given homework expired or not.
        :param homework: an instance of the Homework class that a student is
        going to do.
        :param result: some text as a result for homework
        :return: if deadline hasn't expired return an instance of the
        HomeworkResult class, otherwise:
        Raises:
        DeadlineError if deadline of the homework has expired.
        """
        if homework.is_active():
            return HomeworkResult(self, homework, result)
        raise DeadlineError('You are late')


class Teacher(Person):
    """
    A class describes an instance of a teacher, inherited class Person.
    """
    homework_done = defaultdict(set)

    def __init__(self, *args):
        """
        Method to initialize the object’s attributes
        """
        super(Teacher, self).__init__(*args)

    @staticmethod
    def create_homework(text: str, deadline: int) -> Homework:
        """
        Creates an instance of the Homework class.
        :param text: text of created homework
        :param deadline: int: the number of days to complete this homework
        :return: an instance of Homework class
        """
        return Homework(text, deadline)

    @classmethod
    def check_homework(cls, result: HomeworkResult) -> bool:
        """
        Checks the given homework result. If text of answer is longer than 5
        symbols and doesn't duplicate others, returns True otherwise False.
        If successful, add to homework_done, otherwise do nothing.
        :param result: an instance of the HomeworkResult class
        :return:  True, if homework  is correct, False otherwise
        """
        if len(result.solution) > 5:
            cls.homework_done[result.homework].add(result)
            return True
        return False

    @classmethod
    def reset_results(cls, homework: Homework = None) -> None:
        """
        Resets results of homework. If Homework is given, delete all saved
        solutions. If no argument is given, method reset all results.
        :param homework: an instance of the Homework class (default None)
        """
        if homework:
            cls.homework_done.pop(homework)
        else:
            cls.homework_done.clear()


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')
    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')

    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2
    #
    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results(oop_hw)
