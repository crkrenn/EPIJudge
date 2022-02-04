from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    print(f"preorder: {preorder}")
    print(f"inorder: {inorder}")
    if not preorder:
        return None 
    if not inorder:
        return None 
    root = BinaryTreeNode()
    root_value = preorder[0]
    root.data = root_value
    if len(preorder) == 1:
        return root
    if root_value != inorder[0]:   # there is a a left branch
        new_inorder = inorder[:inorder.index(root_value)] 
        new_preorder = preorder[1:preorder.index(new_inorder[-1])+1]
        left = binary_tree_from_preorder_inorder(new_preorder, new_inorder)
    else:
        left = None
    if root_value != inorder[-1]:   # there is a a right branch
        new_inorder = inorder[inorder.index(root_value)+1:]
        if left == None:
            last_left_value = root_value
        else: 
            last_left_value = inorder[inorder.index(root_value)-1] 
        new_preorder = preorder[preorder.index(last_left_value)+1:]
        right = binary_tree_from_preorder_inorder(new_preorder, new_inorder)
    else:
        right = None 
    root.left = left
    root.right = right
    print(root)
    return root


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
