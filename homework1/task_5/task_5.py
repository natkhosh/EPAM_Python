"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    Function find a sub-array with length less then or equal to "k", with maximal sum.
    :param nums: list of integer numbers
    :param k: length of sub-array
    :return: maximal sum of sub-array
    """
    arr_len = len(nums)
    # max_sum = 0

    if not arr_len :
        return 0

    max_sum = max(nums)
    if k == 1:
        return max_sum
    else:
        for i in range(2, k + 1):
            for j in range(arr_len):
                subarray_sum = sum(nums[j : i + j])
                if subarray_sum > max_sum:
                    max_sum = subarray_sum
        return max_sum
