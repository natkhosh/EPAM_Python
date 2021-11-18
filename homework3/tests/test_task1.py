from homework3.task_1.task_1 import cache


def test_cache():
    """
    Testing that function remembers other function output value.
    Gives out cached value up to "times" number only.
    """
    @cache(times=2)
    def func(a, b):
        return a ** b ** 2

    cache_res_1 = func(5, 2)
    cache_res_2 = func(5, 2)
    cache_res_3 = func(5, 2)
    cache_res_4 = func(8, 2)

    assert cache_res_1 == cache_res_2 == cache_res_3
    assert cache_res_4 != cache_res_3
