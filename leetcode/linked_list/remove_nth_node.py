from typing import Optional
from leetcode.linked_list.reverse_linked_list import ListNode

'''
Leetcode #19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

This can be achieved pretty simply by using two pointers and starting the left pointer on a dummy node with dummy.next = head. 
The right pointer is the node n steps away from head.
'''


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(-1, head)
    l = dummy
    r = head
    while n > 0 and r:
        r = r.next
        n -= 1

    while r:
        print(f"left: {l.val}, right: {r.val}")
        l = l.next
        r = r.next

    l.next = l.next.next

    return dummy.next
