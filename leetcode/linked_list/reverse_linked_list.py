'''
Leetcode #206

Reverse a linked list iterively and recursively
'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next=None




def reverseLinkedListIter(head: Optional[ListNode]) -> Optional[ListNode]: 
    prev, curr = None, head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

def reverseLinkedListRecursive(head: Optional[ListNode]) -> Optional[ListNode]:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
            

        
