from test_framework import generic_test

#918 - 930

import math

def reverse(x: int) -> int:
    # TODO - you fill in here.
    negative = x < 0
    if negative:
        x = - x
    result = 0
    exp_result = 0
    exp_source = math.floor(math.log10(x))
    while x > 0:
        power_of_ten = 10 ** (exp_source)
        digit = x // power_of_ten
        result += digit * 10 ** exp_result
        exp_result += 1
        exp_source -= 1
        x -= digit * power_of_ten
    if negative:
        result = - result
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
