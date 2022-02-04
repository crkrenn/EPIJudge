import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3

# 16.1 THE TOWERS OF HANOI PROBLEM A peg contains rings in sorted order, with
# the largest ring being the lowest. You are to transfer these rings to another
# peg, which is initially empty. This is illustrated in Figure 16.1. PI P2 P3
# PI P2 P3 (a) Initial configuration. (b) Desired configuration. Figure 16.1:
# Tower of Hanoi with 6 pegs. Write a program which prints a sequence of
# operations that transfers n rings from one peg to another. You have a third
# peg, which is initially empty. The only operation you can perform is taking a
# single ring from the top of one peg and placing it on the top of another peg.
# You must never place a larger ring above a smaller ring. Hint: If you know
# how to transfer the top n —1 rings, how does that help move the nth ring?

peg_map = {
    (1, 2): 0,
    (2, 1): 0,
    (1, 0): 2,
    (0, 1): 2,
    (2, 0): 1,
    (0, 2): 1
}

# 3: move 2 old other; move 1 old new; move 2 other, new

def move_n(n: int, old: int, new: int) -> List[List[int]]:
    if n == 1:
        return [[old, new]]
    # print()
    # print(peg_map)
    # print((old,new))
    other = peg_map[(old, new)]
    # if n == 2:
    #     return [[old, other], [old, new], [other, new]]
    result = []
    result.extend(move_n(n-1, old, other))
    result.extend(move_n(1, old, new))
    result.extend(move_n(n-1, other, new))
    return result


def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
    return move_n(num_rings, 0, 2)

@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure('Illegal move from {} to {}'.format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('hanoi.py', 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
