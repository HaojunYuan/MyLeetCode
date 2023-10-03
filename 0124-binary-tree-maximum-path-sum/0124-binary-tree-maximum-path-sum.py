# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        partial, total = self.process(root)
        return total
    
    def process(self, node):
        if not node:
            return 0, -math.inf
        
        left, leftMax = self.process(node.left)
        right, rightMax = self.process(node.right)
        left = max(0, left)
        right = max(0, right)
        partial = max(max(left, right) + node.val, 0)
        total = max(leftMax, rightMax, left + right + node.val)
        return partial, total