# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 

        currHead = head

        while currHead:
            next = currHead.next
            currHead.next = prev
            prev = currHead
            currHead = next
        
        return prev
