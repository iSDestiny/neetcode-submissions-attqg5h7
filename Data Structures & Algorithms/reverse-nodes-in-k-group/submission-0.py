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
            print("ops" ,opsLeft)
            current = prevHead
            prev = None
            if current:
                print(current.val)
            if prev:
                print(prev.val)
            else:
                print(None)
            for _ in range(k):
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
            if current:
                print(current.val)
                print(prev.val)
            # at the end current is the head of the next k and prev is the head of the first k
            if opsLeft == count // k:
                firstPrev = prev
            if prevTail:
                print("prevtail", prevTail.val)
                prevTail.next = prev
            # new prev tail becomes the original head of this set of k nodes
            prevTail = prevHead
            prevHead = current
            opsLeft -= 1
        if prevTail:
            prevTail.next = prevHead
 

        return firstPrev            
