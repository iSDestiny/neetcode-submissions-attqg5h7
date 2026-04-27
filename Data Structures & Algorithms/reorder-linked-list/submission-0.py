# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # Get the middle node
        slow = fast = head 
        prevSlow = None
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            prevSlow = slow
            slow = slow.next

        # Set this to None so we don't infinite loop when we interleave 
        prevSlow.next = None 

        # Reverse the right half
        prevSlow = None
        while slow:
            oldNext = slow.next
            slow.next = prevSlow
            prevSlow = slow
            slow = oldNext
        
        # Interleave
        forward = head
        reverse = prevSlow

        while forward and reverse:
            oldForwardNext = forward.next
            oldReverseNext = reverse.next
            forward.next = reverse
            reverse.next = oldForwardNext
            forward = oldForwardNext
            reverse = oldReverseNext
        
