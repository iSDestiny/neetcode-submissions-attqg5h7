# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = head = ListNode(0) 

        carry = 0
        while l1 or l2:
            currSum = 0
            if l1 and l2:
                currSum = l1.val + l2.val + carry
            elif l1:
                currSum = l1.val + carry
            else:
                currSum = l2.val + carry
            
            if currSum > 9:
                carry = 1
            else:
                carry = 0
            
            l3.next = ListNode(currSum%10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            l3 = l3.next
        if carry > 0:
            l3.next = ListNode(carry)
        return head.next