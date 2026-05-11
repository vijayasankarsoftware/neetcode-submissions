# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()

            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
        return ",".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if nodes[i] != "null":
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            i += 1
            if nodes[i] != "null":
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i += 1
        return root

