# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head:
            return

        stack = []

        slow = head
        fast = head

        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # push second half into stack
        while slow:
            stack.append(slow)
            slow = slow.next

        current = head

        # reorder
        while stack:

            last = stack.pop()

            # stop condition
            if current == last or current.next == last:
                last.next = None
                break

            temp = current.next

            current.next = last
            last.next = temp

            current = temp