from typing import Optional
from leetcode.linked_list.reverse_linked_list import ListNode

'''
Leetcode #141 Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''


# Using Set
def hasCycle(self, head: Optional[ListNode]) -> bool:
    visited = set()
    node = head

    while node:
        if node in visited:
            return True
        else:
            visited.add(node)
            node = node.next

    return False

# Two Pointer


def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True

    return False
