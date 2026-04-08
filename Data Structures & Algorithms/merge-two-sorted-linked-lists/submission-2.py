# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    #                 v
    # 1 -> 2 -> 4 -> None
    #                 v
    # 1 -> 3 -> 5 -> None
    #
    # newlist: 1 -> 1 -> 2 -> 3 -> 4 -> 5
    # 
    # Time: O(n+m)
    # Space: O(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2

        if not l1:
            return l2
        if not l2:
            return l1
        
        frontHead = None
        if l1.val <= l2.val:
            frontHead = l1
            l1 = l1.next
        else:
            frontHead = l2
            l2 = l2.next

        current = frontHead
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
            elif l1:
                current.next = l1
                l1 = l1.next
            elif l2:
                current.next = l2
                l2 = l2.next

            current = current.next

        return frontHead
    
