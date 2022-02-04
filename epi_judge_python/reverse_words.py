import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# 921

# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    # # TODO - you fill in here.
    # print(s)
    # s = list(" ".join(reversed("".join(s).split())))
    # print(s)
    # print(list(" ".join(reversed("".join(s).split()))))
    # return s
    new_s = []
    i = len(s) - 1
    length = len(s)
    while i >= 0:
        while s[i] != " " and i > 0:
            i -= 1
        s, word = s[:i], s[i+1:]
        new_s.extend(word)
        new_s.append(" ")
        i -= 1
    new_s = new_s[:length]
    s, new_s = new_s, s
# reverse_words(['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'])


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
