# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, l, r):
            nonlocal res
            if node.left: 
                dfs(node.left,r+1,0)
            if node.right:
                dfs(node.right,0,l+1)
            res = max(res,l,r)
        dfs(root,0,0)
        return res
