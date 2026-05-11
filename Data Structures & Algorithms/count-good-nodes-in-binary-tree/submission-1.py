# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maximum, count):
            if not node:
                return 0
            if node.val >= maximum:
                count = 1
            else:
                count = 0

            maximum = max(maximum, node.val) 
            left = dfs(node.left, maximum, count)
            right = dfs(node.right, maximum, count)
            return count + left + right

        return dfs(root, root.val, 0)
        

            