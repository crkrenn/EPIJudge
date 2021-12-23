from test_framework import generic_test

# from icecream import ic

# make lookup
lookup = {}
for i in range(2**(64//4)):
    parity = 0
    j = i 
    while j > 0:
        if j & 1:
            if parity:
                parity = 0
            else:
                parity = 1
        j = j >> 1
    lookup[i] = parity
print("done")
# for i in lookup:
#     print(i, lookup[i])


def parity(x: int) -> int:
    parity = 0
    mask = 2**(64//4) - 1
    j = x
    for i in range(4):
        k = j & mask
        if lookup[k]:
            if parity:
                parity = 0
            else:
                parity = 1
        j = j >> (64//4)

    # TODO - you fill in here.

    return parity


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
