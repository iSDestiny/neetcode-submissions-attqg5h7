# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.orderMap = {val: key for key, val in enumerate(inorder)}
        self.preorder = preorder
        self.pIndex = 0
        return self.dfs(0, len(inorder)-1)

    def dfs(self, left: int, right: int) -> Optional(TreeNode):
        if left > right:
            return None
        rootVal = self.preorder[self.pIndex]
        self.pIndex += 1
        mid = self.orderMap[rootVal]
        root = TreeNode(rootVal)
        root.left = self.dfs(left, mid-1)
        root.right = self.dfs(mid+1, right)

        return root