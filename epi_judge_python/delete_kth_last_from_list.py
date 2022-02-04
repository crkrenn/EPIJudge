from typing import Optional

from list_node import ListNode
from test_framework import generic_test

#9:37
# Assumes L has at least k nodes, deletes the k-th last node in L.
# cases: single node, middle node, last node, first node
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    print(f"LL:{L}")
    head = L
    kth_node_minus_one = L
    node = L 
    count = 0
    while node and count < k:
        node = node.next
        count += 1
    if not node:
        print(f"head.next: {head.next}")
        return head.next
    while node:
        node = node.next
        if node:
            kth_node_minus_one = kth_node_minus_one.next 
    kth_node_minus_one.next = kth_node_minus_one.next.next
    print(f"head: {head}")
    return head

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
