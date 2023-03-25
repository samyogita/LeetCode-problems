from collections import Counter, defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.res = []
        mp = defaultdict(int)
        def dfs(node):
            if not node:
                return ""
            cur = f"(({dfs(node.left)}){node.val}({dfs(node.right)}))"
            print(cur)
            mp[cur] += 1
            if mp[cur] == 2:
                self.res.append(node)
            return cur

        dfs(root)

        return self.res
