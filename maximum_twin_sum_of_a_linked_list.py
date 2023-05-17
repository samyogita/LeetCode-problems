# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = None
        while slow:
            tmp = slow.next
            slow.next = rev
            rev, slow = slow, tmp
        res = 0
        while rev:
            res = max(res, rev.val + head.val)
            rev, head = rev.next, head.next
        return res
