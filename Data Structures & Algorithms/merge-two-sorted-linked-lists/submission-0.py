# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1 = list1
        l2 = list2
        l_head = ListNode(0)
        current = l_head
        while l1 and l2:
            if l1.val <= l2.val:
                new_node = ListNode(l1.val)
                current.next = new_node
                current = new_node
                l1 = l1.next
            else:
                new_node = ListNode(l2.val)
                current.next = new_node
                current = new_node
                l2 = l2.next
        
        if l1:
            current.next = l1
        if l2:
            current.next = l2

        return l_head.next
