from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def height_and_balance_tree(tree: BinaryTreeNode) -> (int, bool):
    if tree == None:
        return (0, True)
    h_left, b_left = height_and_balance_tree(tree.left)
    h_right, b_right = height_and_balance_tree(tree.right)
    if not b_left or not b_right:
        return (0, False)
    if abs(h_left - h_right) >= 2:
        return (0, False)
    return (max(h_left, h_right) + 1, True)


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    return height_and_balance_tree(tree)[1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
