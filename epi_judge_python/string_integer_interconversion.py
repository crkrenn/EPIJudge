from test_framework import generic_test
from test_framework.test_failure import TestFailure

import math

def int_to_string(x: int) -> str:
    if x == 0:
        return '0'
    result = []
    ord0 = ord('0')
    if x < 0:
        negative = True
        x = - x 
    else:
        negative = False
    while x > 0:
        lsd = x % 10
        x = x // 10
        result.append(chr(ord0 + lsd))
    if negative:
        result.append('-')
    else:
        result.append('+')
    return ''.join(list(reversed(result)))


def string_to_int(s: str) -> int:
    if s == '0':
        return 0
    result = 0
    exp = 0
    ord0 = ord('0')
    for char in reversed(s):
        if char == '-':
            result = - result
        elif char == '+':
            pass
        else:
            result += (ord(char) - ord0) * 10 ** exp
        exp += 1
    return result



def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
