
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        null_found = False
        dq = deque([root])
        while dq:
            cur = dq.popleft()
            if cur:
                if null_found:
                   return False
                dq.append(cur.left)
                dq.append(cur.right)
            else:
                null_found = True
        return True
