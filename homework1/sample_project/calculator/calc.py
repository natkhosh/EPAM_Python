def check_power_of_2(a: int) -> bool:
    """
    Function to find,  if given a positive integer is a power of two or not.
    :param a: integer
    :return: bool: true for success if the given integer is a power of two,
    False otherwise.
    """
    return not (bool(a & (a - 1))) and a > 0
