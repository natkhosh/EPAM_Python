"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
from enum import Enum
class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"
class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"
Should become:
class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")
class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


class SimplifiedEnum(type):
    """
    Simplified version of Enum class without duplications in variables
    declarations.
    """
    def __new__(cls, name, bases, attrs):
        """
        Creates a new class with given name, bases and attributes.
        :param name: of new class
        :param bases: ancestor class or classes, could be empty
        :param attrs: name space of new class
        """
        key = f"_{name}__keys"
        attrs = {key: key for key in attrs[key]}

        return super().__new__(cls, name, bases, attrs)
