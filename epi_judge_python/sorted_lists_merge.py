from typing import Optional

from list_node import ListNode
from test_framework import generic_test

#710 | 736
# edge cases: either/both blank
# assume no elements are equal
# could combine if then logic
# self.data; self.next
def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    if not L1:
        return L2
    if not L2:
        return L1
    l1_ptr = L1
    l2_ptr = L2
    if l1_ptr.data < l2_ptr.data:
        result = L1
        l1_ptr = l1_ptr.next
    else:
        result = L2 
        l2_ptr = l2_ptr.next
    last = result 
    while l1_ptr and l2_ptr:
        if l1_ptr.data < l2_ptr.data:
            last.next = l1_ptr
            l1_ptr = l1_ptr.next
        else:
            last.next = l2_ptr
            l2_ptr = l2_ptr.next
        last = last.next
    if l1_ptr:
        last.next = l1_ptr
    else:
        last.next = l2_ptr         
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
