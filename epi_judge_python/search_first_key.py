from typing import List

from test_framework import generic_test

import bisect

def search_first_of_k(A: List[int], k: int) -> int:
    # TODO - you fill in here.
    result = bisect.bisect_left(A, k)
    if result >= len(A):
        return -1
    if k != A[result]:
        return -1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
