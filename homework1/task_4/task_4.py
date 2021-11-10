"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """
    Function compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
    :param a , b, c, d:  list of integer values, have same length of N where 0 ≤ N ≤ 1000
    :return: integer, amount of found tuples with sum of items is zero
    """
    sums = {}
    for i in a:
        for j in b:
            if i + j not in sums:
                sums[i + j] = 1
            else:
                sums[i + j] += 1
    counter = 0
    for i in c:
        for j in d:
            if -1 * (i + j) in sums:
                # print(-1 * (i+j))
                counter += sums[-1 * (i + j)]
        return counter


print(check_sum_of_four([0, 1], [-1, 0], [1, 0], [0, -1]))
