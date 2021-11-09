"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    ...


# arr1 = [1, 2]
# arr2 = [3, 5]
# sum_ = []
# for i in range(len(arr1)):
#     for j in range(len(arr1)):
#         sum_.append(arr1[i] + arr2[j])
#         print(sum_)

#
# def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
#     ...
