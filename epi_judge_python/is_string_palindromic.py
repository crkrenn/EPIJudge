from test_framework import generic_test

# 9:16 - 9:18

def is_palindromic(s: str) -> bool:
    # TODO - you fill in here.
    i = 0
    j = len(s) - 1
    while j > i:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
