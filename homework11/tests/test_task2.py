from typing import Callable, Union

import pytest

from homework11.task_2.task_2 import Order, elder_discount, morning_discount


@pytest.mark.parametrize('price, function, expected_result',
                         [(100, morning_discount, 75.0),
                          (100, elder_discount, 10.0)
                          ])
def test_Order_class_with_discount(price: Union[float, int],
                                   function: Union[Callable, None],
                                   expected_result: float):
    """
    Testing that the price calculated according to the additional
    discount program.
    :param price: order price
    :param function: additional discount program
    :param expected_result: total price
    """
    order_1 = Order(price, function)
    order_2 = Order(price, function)

    assert order_1.final_price() == expected_result
    assert order_2.final_price() == expected_result


@pytest.mark.parametrize('price, expected_result',
                         [(100, 100.0),
                          (70, 70.0)
                          ])
def test_Order_class_without_discount(price: Union[float, int],
                                      expected_result: float):
    """
    Testing that the price calculated without to the additional
    discount program.
    :param price: order price
    :param expected_result: total price
    """
    order_3 = Order(price)
    assert order_3.final_price() == expected_result
