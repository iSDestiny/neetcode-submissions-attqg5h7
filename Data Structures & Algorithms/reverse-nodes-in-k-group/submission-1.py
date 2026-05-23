# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # get the number of nodes
        current = head
        count = 0
        while current:
            count += 1
            current = current.next
        
        opsLeft = count // k
        firstPrev = None
        prevTail = None
        prevHead = head
        while opsLeft:
            current = prevHead
            prev = None
            for _ in range(k):
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
            # at the end current is the head of the next k and prev is the head of the first k
            if opsLeft == count // k:
                firstPrev = prev
            if prevTail:
                prevTail.next = prev
            # new prev tail becomes the original head of this set of k nodes
            prevTail = prevHead
            prevHead = current
            opsLeft -= 1
        if prevTail:
            prevTail.next = prevHead
 

        return firstPrev            
