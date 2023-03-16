# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.n = len(inorder)-1
        mp = {v:k for k, v in enumerate(inorder)}
        def dac(l, r):
            if l> r:
                return None
            cur = postorder[self.n]
            root = TreeNode(cur)
            self.n -= 1
            mid = mp[cur]
            root.right = dac(mid+1, r)
            root.left = dac(l, mid-1)
            return root
        return dac(0, len(inorder)-1)


            

        
