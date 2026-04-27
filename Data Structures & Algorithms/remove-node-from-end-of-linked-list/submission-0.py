# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        num = 0
        slow = fast = head 
        prevSlow = None
        while fast:
            fast = fast.next
            if num >= n:
                prevSlow = slow
                slow = slow.next
            num += 1
        
        print(slow.val)

        if prevSlow:
            prevSlow.next = prevSlow.next.next
            return head
        return head.next
        