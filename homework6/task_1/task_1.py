"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    """Decorator for counting instances of a class."""
    cls.counter = 0

    def __new__(self):
        """
        A class is instantiated __new__ method.
        Increments counter by one if a new class instance is created.
        :return: An instance of received class
        """
        instance = super(cls, self).__new__(self)
        self.counter += 1
        return instance

    def get_created_instances(*args) -> int:
        """
        Method returns the count of created class instances.
        :param args: any class
        :return: count of instances
        """
        return cls.counter

    def reset_instances_counter(*args) -> int:
        """
        Method resets counter and returns previous value
        :param args: any class
        :return: count of instances before reset
        """
        tmp_counter = cls.counter
        cls.counter = 0
        return tmp_counter

    cls.__new__ = __new__
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter

    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    # user = User()
    print(user.get_created_instances())  # 3
    print('tmp_counter ', user.reset_instances_counter())  # 3
