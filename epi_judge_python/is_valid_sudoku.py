from typing import List

from test_framework import generic_test


# 944 1003
# row, column, subgrid

# Check if a partially filled matrix has any conflicts.

digits = set(range(1,10))

def check_row_column(grid: List[List[int]])-> bool:
    for i in range(9):
        seen_set_1 = set()
        seen_set_2 = set()
        for j in range(9):
            digit = grid[i][j]
            if digit in digits:
                if digit in seen_set_1:
                    return False
                else:
                    seen_set_1.add(digit)
            digit = grid[j][i]
            if digit in digits:
                if digit in seen_set_2:
                    return False
                else:
                    seen_set_2.add(digit)
    return True

def check_boxes(grid: List[List[int]])-> bool:
    corner_list = [[0,0], [0,3], [0,6],
                   [3,0], [3,3], [3,6],
                   [6,0], [6,3], [6,6]]
    offset_list = [[0,0], [0,1], [0,2],
                   [1,0], [1,1], [1,2],
                   [2,0], [2,1], [2,2]]
    for i0, j0 in corner_list:
        seen_set = set()
        for i, j in offset_list:
            digit = grid[i0+i][j0+j]
            if digit in digits:
                if digit in seen_set:
                    return False
                else:
                    seen_set.add(digit)
    return True

def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # TODO - you fill in here.
    return check_boxes(partial_assignment) and check_row_column(partial_assignment)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
