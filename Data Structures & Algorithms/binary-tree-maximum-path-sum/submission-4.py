# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        def dfs(r) -> int:
            if not r:
                return 0

            left_max = dfs(r.left)
            right_max = dfs(r.right)

            # return left or right max if non negative
            down_max = max(left_max, right_max, 0)

            # current is the split
            self.max_sum = max(self.max_sum, left_max + r.val + right_max) 
            self.max_sum = max(self.max_sum, r.val + down_max)

            return r.val + down_max
        
        dfs(root)
        
        return self.max_sum