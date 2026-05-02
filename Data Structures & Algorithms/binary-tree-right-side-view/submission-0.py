# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        res = []

        while queue:
            target = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                target = node.val
                queue.append(node.left)
                queue.append(node.right)
            if target:
                res.append(target)
        return res 