# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, interval):
            if not node:
                return True
            return interval[0] < node.val < interval[1] and dfs(node.left, (interval[0], node.val)) and dfs(node.right, (node.val, interval[1]))
        return dfs(root, (float('-inf'), float('inf')))