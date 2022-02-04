import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


# [2, 2, 2, 2]; p = 2; pass (all eq)
# [1, 2, 2, 2]; p = 1; pass (all gt)
# [2, 2, 1, 2]; p = 2; pass (all gt)
# [2, 1, 1, 1]; p = 1; 

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    lt_idx = 0
    eq_idx = 1
    gt_idx = 1
    idx = 1
    pivot = A[pivot_index]
    A[0], A[pivot_index] = A[pivot_index], A[0]
    while idx < len(A):
        if A[idx] > pivot:
            gt_idx += 1
        elif A[idx] == pivot:
            A[idx], A[eq_idx] = A[eq_idx], A[idx]
            eq_idx += 1
            gt_idx += 1
        else:
            A[idx], A[eq_idx] = A[eq_idx], A[idx]
            A[lt_idx], A[eq_idx] = A[eq_idx], A[lt_idx]
            lt_idx += 1
            eq_idx += 1
            gt_idx += 1
        idx += 1
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
