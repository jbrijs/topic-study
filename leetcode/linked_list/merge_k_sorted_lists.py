from typing import List, Optional
from leetcode.linked_list.reverse_linked_list import ListNode


'''
Leetcode #23 Merge k Sorted Lists

Go through list in lists, and merge the lists using a helper function
'''



def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_list = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_list.append(self.mergeLists(l1, l2))
            lists = merged_list
        return lists[0]

        
def mergeLists(self, l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    if l1:
        tail.next = l1
    else:
        tail.next = l2
    return dummy.next
                

                   

        