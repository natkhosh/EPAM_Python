from homework6.task_1.task_1 import instances_counter


@instances_counter
class SomeClass:
    """Creating sample instances"""
    pass


def test_instances_counter():
    """
    Testing that an instance counter of a class equals the number of
    created instances
    """

    assert SomeClass.get_created_instances() == 0
    inst1 = SomeClass()
    assert inst1.get_created_instances() == 1
    inst2 = SomeClass()
    assert inst2.get_created_instances() == 2


def test_reset_instances_counter():
    """
    Testing that an instance counter of a class got reset counter
    """
    inst1 = SomeClass()
    assert inst1.get_created_instances() == 3
    inst1.reset_instances_counter()
    assert inst1.reset_instances_counter() == 0
    assert inst1.get_created_instances() == 0
