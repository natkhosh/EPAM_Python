import time

from homework3.task_2.task_2 import sum_slow_calculate


def test_sum_slow_calculate():
    """
    Testing that function calculate total sum of slow_calculate().
    """
    assert sum_slow_calculate() == 1025932


def test_timer_func():
    """
    Testing that function calculation time should not take more than a minute.
    """
    start_time = time.time()
    sum_slow_calculate()
    sec = time.time() - start_time

    assert sec <= 60
    print(f"Calculation time: {sec:.2f} seconds")
