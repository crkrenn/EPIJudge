from typing import List

from test_framework import generic_test

import heapq

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    heap = heapq.merge(*sorted_arrays)
    length_arrays = sum([len(array) for array in sorted_arrays])
    result = []
    for item in heapq.nsmallest(length_arrays, heap):
        result.append(item)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
