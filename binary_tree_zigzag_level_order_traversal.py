# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        flip = False
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            m = len(q)
            cur = []
            for i in range(m):
                node = q.popleft()
                cur.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not flip:
                res.append(cur)
                
            else:
                res.append(cur[::-1])
            flip ^= 1

        return res
