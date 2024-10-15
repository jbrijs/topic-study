from typing import Optional
from leetcode.linked_list.reverse_linked_list import ListNode

'''
Leetcode #2 Add Two Numbers

Given two linked lists representing a number in reverse order, return a new linked list representing
the sum of these numbers in reverse order

Pretty simple, use a dummy node to start your new list. Keep track of carry and val using mod and 
integer division.
'''


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()

    carry = 0
    node = dummy
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        val = v1 + v2 + carry
        carry = val // 10
        val = val % 10

        node.next = ListNode(val, None)

        node = node.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next
