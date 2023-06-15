from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        mx = root.val
        lvl, res = 0, mx
        while q:
            lvl += 1
            m = len(q)
            nq = []
            for i in range(m):
                node = q.popleft() 
                nq.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if mx < sum(nq):
                mx, res = sum(nq), lvl
        return res
