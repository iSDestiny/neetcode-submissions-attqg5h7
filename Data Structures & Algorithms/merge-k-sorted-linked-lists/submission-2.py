# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time: O(nlogk)
# Space: O(k)

from heapq import heapify, heappush, heappop

class Solution:    
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     heap = []
    #     for i, ln in enumerate(lists):
    #         if ln: # dont process empty ll
    #             heap.append((ln.val, i, ln))
        
    #     heapify(heap) # O(k)
        
    #     head = ListNode()
    #     current = head
    #     while heap:
    #         val, id, ln = heappop(heap)
    #         current.next = ListNode(val)
    #         current = current.next
    #         if ln.next:
    #             heappush(heap, (ln.next.val, id, ln.next))
        
    #     return head.next
            
            
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                listA = lists[i]
                listB = lists[i+1] if i+1 < len(lists) else None
                merged.append(self.mergeLists(listA, listB))

            lists = merged

        return lists[0]


    
    def mergeLists(self, listA: List[Optional[ListNode]], listB: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        current = head

        while listA and listB:
            if listA.val <= listB.val:
                current.next = ListNode(listA.val)
                listA = listA.next
            else:
                current.next = ListNode(listB.val)
                listB = listB.next

            current = current.next
        
        if listA:
            current.next = listA
        else:
            current.next = listB
        
        return head.next