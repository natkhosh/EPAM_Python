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

    if arr_len > 1 and 1 < k <= arr_len:
        max_sum = nums[0]

        for i in range(0, arr_len - k + 1):
            for j in range(2, k + 1):
                # Sum definition, the aggregate of two or more numbers
                subarray_sum = sum(nums[i : i + j])
                if subarray_sum > max_sum:
                    max_sum = subarray_sum
        return max_sum
    return 0
