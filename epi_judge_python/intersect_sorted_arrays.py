from typing import List

from test_framework import generic_test

from collections import deque

# 1242

def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    # TODO - you fill in here.
    print()
    # print(f"A: {A}")
    # print(f"B: {B}")
    if not A or not B:
        return []
    aq = deque(A)
    bq = deque(B)
    a = aq.popleft()
    b = bq.popleft()
    result = []
    while a != None and b != None:
        # print(f"a/b/result: {a}/{b}/{result}")
        if a == b:
            if not result:
                result.append(a)
            elif a != result[-1]:
                result.append(a)
            if aq and bq:
                a = aq.popleft()
                b = bq.popleft()  
            else:
                a, b = None, None          
        elif a < b:
            if aq:
                a = aq.popleft()
            else:
                a = None
        else:
            if bq:
                b = bq.popleft()
            else:
                b = None
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
