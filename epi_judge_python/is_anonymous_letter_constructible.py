from test_framework import generic_test

from collections import Counter

#104

def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    # TODO - you fill in here.
    counter = Counter(letter_text)
    if not counter:
        return True
    for char in magazine_text:
        if char in counter:
            counter[char] -= 1
            if counter[char] == 0:
                del counter[char]
            if not counter:
                return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
