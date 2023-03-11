# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def dac(l, r):
            if l > r:
                return None
            mid = (l+r) // 2
            root = TreeNode(self.A[mid])
            root.left = dac(l, mid-1)
            root.right = dac(mid+1, r)
            return root

        self.A = []
        while head:
            self.A.append(head.val)
            head = head.next
        
        return dac(0, len(self.A)-1)

