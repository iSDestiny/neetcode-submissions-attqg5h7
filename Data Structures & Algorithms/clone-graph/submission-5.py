"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        root = Node(0, [])
        clones = {}

        def dfs(current: Optional['Node']):
            if current.val in clones:
                return clones[current.val]
            newClone = Node(current.val)
            clones[current.val] = newClone
            
            for n in current.neighbors:
                newClone.neighbors.append(dfs(n))
            return newClone
        
        return dfs(node)