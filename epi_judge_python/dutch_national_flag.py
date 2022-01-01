import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # count_0 = A.count(0)
    # count_1 = A.count(1)
    # count_2 = A.count(2)
    # for i in range(len(A)):
    #     if i < count_0:
    #         A[i] = 0
    #     elif i < count_0 + count_1:
    #         A[i] = 1
    #     else:
    #         A[i] = 2
    

    # TODO - you fill in here.
    print()
    print("in", A)
    lt_right_index = 0
    eq_right_index = 0
    i = 0
    pivot = A[pivot_index]
    while i < len(A):
        a = A[i]
        if a > pivot:
            i = i + 1
        elif lt_right_index == eq_right_index:
            if a < pivot:
                A[lt_right_index], A[i] = A[i], A[lt_right_index]
                lt_right_index = lt_right_index + 1
                eq_right_index = eq_right_index + 1
            if a == pivot:
                A[eq_right_index], A[i] = A[i], A[eq_right_index]
                eq_index = eq_right_index + 1
            i = i + 1
        else:
            if a < pivot:
                A[eq_index], A[i] = A[i], A[eq_index]
                A[lt_right_index], A[eq_index] = A[eq_index], A[lt_right_index]
                lt_right_index = lt_right_index + 1
                eq_right_index = eq_right_index + 1
            if a == pivot:
                A[eq_right_index], A[i] = A[i], A[eq_right_index]
                eq_right_index = eq_right_index + 1
            i = i + 1
    print("out:", A)
    return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
