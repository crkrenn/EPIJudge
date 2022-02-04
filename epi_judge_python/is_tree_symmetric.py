from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# 915
# 924

def is_symmetric_helper(treeA: BinaryTreeNode, treeB: BinaryTreeNode)-> bool:
    if treeA == None and treeB == None:
        return True
    if treeA == None or treeB == None:
        return False
    if treeA.data != treeB.data:
        return False
    return (
        is_symmetric_helper(treeA.left, treeB.right)
        and is_symmetric_helper(treeA.right, treeB.left))


def is_symmetric(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    if tree == None:
        return True
    return is_symmetric_helper(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
