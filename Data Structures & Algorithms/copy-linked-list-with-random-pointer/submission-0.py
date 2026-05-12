"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return head

        mapping = {}

        current = head

        while current:
            copy_node = Node(current.val)

            mapping[current] = copy_node

            current = current.next

        current = head

        while current:

            copy_node = mapping[current]
            
            copy_node.next = mapping.get(current.next)
            copy_node.random = mapping.get(current.random)

            current = current.next

        return mapping[head]
        