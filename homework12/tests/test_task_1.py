from homework12.task_1.task_1_CRUD import session_scope
from homework12.task_1.task_1_models import Student, Teacher

DATABASE = 'sqlite:///../task_1/main.db'


def test_database_structure():
    """Testing that all created records exist in database"""
    with session_scope(DATABASE) as session:

        student = session.query(Student).all()
        teacher = session.query(Teacher).all()

        assert student[0].last_name == "Petrov"
        assert teacher[0].first_name == 'Daniil'


def test_recording_student():
    """Testing that new record created and exist in database"""
    with session_scope(DATABASE) as session:
        student = Student(first_name='Natalia', last_name='Khoshina')
        session.add(student)

        student = session.query(Student).\
            filter(Student.first_name == "Natalia").first()
        assert student.last_name == "Khoshina"
