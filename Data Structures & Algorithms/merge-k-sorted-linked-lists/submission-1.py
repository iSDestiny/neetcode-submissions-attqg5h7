# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time: O(nlogk)
# Space: O(k)

from heapq import heapify, heappush, heappop

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, ln in enumerate(lists):
            if ln: # dont process empty ll
                heap.append((ln.val, i, ln))
        
        heapify(heap) # O(k)
        
        head = ListNode()
        current = head
        while heap:
            val, id, ln = heappop(heap)
            current.next = ListNode(val)
            current = current.next
            if ln.next:
                heappush(heap, (ln.next.val, id, ln.next))
        
        return head.next
            
            