from homework11.task_1.task_1 import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


def test_SimplifiedEnum_class():
    """
    Testing that class remove duplications in variables declarations
    using metaclass.
    """
    assert ColorsEnum.RED == "RED"
    assert SizesEnum.XL == "XL"
