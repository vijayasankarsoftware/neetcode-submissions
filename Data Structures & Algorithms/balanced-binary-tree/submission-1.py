# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        def dfs(node):
            if not node:
                return True
            if abs(get_height(node.left) - get_height(node.right)) > 1:
                return False
            if not dfs(node.left) or not dfs(node.right):
                return False
            
            return True
        return dfs(root)

            