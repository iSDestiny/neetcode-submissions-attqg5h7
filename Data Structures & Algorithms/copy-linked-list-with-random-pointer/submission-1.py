"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create a clone for each node and set it as the original's next
        if not head:
            return None
        current = head
        while current:
            clone = Node(current.val)
            nextNode = current.next
            current.next = clone
            clone.next = nextNode 
            current = nextNode
        
        current = head
        while current:
            clone = current.next
            if current.random:
                clone.random = current.random.next
            current = clone.next

        current = head
        newHead = head.next
        while current:
            clone = current.next
            current.next = clone.next
            if clone.next:
                clone.next = clone.next.next
            current = current.next
        
        return newHead

