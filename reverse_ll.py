# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr, rev = head, None
        while ptr:
            temp = ptr.next
            ptr.next = rev
            rev = ptr
            ptr = temp
        return rev
        
        