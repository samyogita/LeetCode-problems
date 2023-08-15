# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr, cur = ListNode(0), ListNode(0)
        b_curr, a_curr = curr, cur
        
        while head:
            if head.val < x:
                b_curr.next, b_curr = head, head
            else:
                a_curr.next, a_curr = head, head
            head = head.next
        
        a_curr.next = None
        b_curr.next = cur.next
        
        return curr.next
        
