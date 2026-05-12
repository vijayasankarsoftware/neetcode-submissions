# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0

        current = head

        while current:
            length += 1
            current = current.next

        element = (length - n)

        j = 0

        current = head
        prev = None

        while current:

            if j == element:
                if not prev:
                    head = current.next
                    break
                else:
                    prev.next = current.next
            j += 1 
            prev = current
            current = current.next

        return head


