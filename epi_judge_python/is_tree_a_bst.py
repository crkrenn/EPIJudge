from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# less: left; >= right; self.data; self.left; self.right
# test cases: None: none left only

def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def valid_max_min(tree: BinaryTreeNode, t_max=float("Inf"), t_min=float("-Inf")):
        if not tree:
            print(f"not tree: {tree}")
            return True
        print(f'node: {tree.data}')
        if not t_min <= tree.data < t_max:
            print(f"min/data/max: {t_min}/{tree.data}/{t_max}")
            return False
        if tree.left:
            print(f'left: {tree.left.data}')
        else:
            print(f'left: {None}')
        if tree.right:
            print(f'right: {tree.right.data}')
        else:
            print(f'right: {None}')
        return (
            valid_max_min(tree.left, t_min=t_min, t_max=tree.data)
            and valid_max_min(tree.right, t_min=tree.data, t_max=t_max))
    print()
    print(tree)
    result = valid_max_min(tree)
    print(f"result: {result}")
    return result

if __name__ == '__main__':
    node = BinaryTreeNode(5)
    node.left = BinaryTreeNode(4)
    node.right = BinaryTreeNode(6)
    node.left.right = BinaryTreeNode(5)
    node.right.left = BinaryTreeNode(5)
    print(f"edge_case: {is_binary_tree_bst(node)}")
    assert False
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
