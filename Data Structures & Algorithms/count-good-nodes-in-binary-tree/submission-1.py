# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, greatest):
            if not node:
                return 0
            balanced = 0
            if node.val >= greatest:
                balanced = 1
                greatest = node.val
            return balanced + dfs(node.left, greatest) + dfs(node.right, greatest)
        
        return dfs(root, root.val)