class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []

        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        total = 0
        carry = 0
        ans = ListNode()
        while s1 or s2:
            if s1:
                total += s1.pop()
            if s2:
                total += s2.pop()

            ans.val = total % 10
            carry = total // 10
            head = ListNode(carry)
            head.next = ans
            ans = head
            total = carry

        return ans.next if carry == 0 else an
