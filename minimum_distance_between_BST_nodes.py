# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = []
        def inorder(node):
            if node == None:
                return 0
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        sm = float('inf')
        for i in range(1, len(res)):
            sm = min(sm, res[i]- res[i-1])
        return sm
