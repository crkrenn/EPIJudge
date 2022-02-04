from typing import List

from test_framework import generic_test

#932 941

def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    carry = 1
    for i in range(len(A)-1, -1, -1):
        new_digit = A[i] + carry
        if new_digit == 10:
            new_digit = 0
            carry = 1
        else:
            carry = 0
        A[i] = new_digit
    if carry:
        result = [1]
    else:
        result = []
    result.extend(A)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
