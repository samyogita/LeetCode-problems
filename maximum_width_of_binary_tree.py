# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = [(root, 1)]
        while q:
            nq = []
            res = max(res, q[-1][1] -q[0][1] + 1)
            for node,i in q:
                if node.left:
                    nq.append((node.left, 2*i))
                if node.right:
                    nq.append((node.right, 2*i+1))
            q = nq
        return res
