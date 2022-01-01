from typing import List

from test_framework import generic_test

# Design an algorithm that takes as input an array and a number, and determines
# if there are three entries in the array (not necessarily distinct) which add
# up to the specified number. For example, if the array is (11,2,5,7,3) then
# there are three entries in the array which add up to 21 (3,7,11 and 5,5,11).
# (Note that we can use 5 twice, since the problem statement said we can use
# the same entry more than once.) However, no three entries add up to 22.

def has_three_sum(A: List[int], t: int) -> bool:
    # TODO - you fill in here.
    a_set = set(A)
    for i in range(len(A)):
        for j in range(len(A)):
            if t - (A[i] + A[j]) in a_set:
                return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
