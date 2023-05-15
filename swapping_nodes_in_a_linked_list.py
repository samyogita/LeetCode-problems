# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = []
        node = head
        while node:
            res.append(node)
            node = node.next
        res[k-1].val, res[-k].val = res[-k].val, res[k-1].val
        return head
