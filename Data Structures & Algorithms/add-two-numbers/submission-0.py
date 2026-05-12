# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        current = result

        a = l1
        b = l2
        carry = 0

        while a and b:
            s = a.val + b.val + carry
            carry = s // 10
            current.next = ListNode(s%10)
            current = current.next
            a = a.next
            b = b.next

        while a:
            s = a.val + carry
            carry = s // 10
            current.next = ListNode(s%10)
            current = current.next
            a = a.next

        while b:
            s = b.val + carry
            carry = s // 10
            current.next = ListNode(s%10)
            current = current.next
            b = b.next
        if carry:
            current.next = ListNode(carry)
        return result.next
