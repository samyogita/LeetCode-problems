# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        node = head
        while node:
            res.append(node)
            node = node.next
        for i in range(0, len(res)-1,2):
            if i+1 == len(res):
                break
            res[i].val, res[i+1].val = res[i+1].val, res[i].val
        return head
