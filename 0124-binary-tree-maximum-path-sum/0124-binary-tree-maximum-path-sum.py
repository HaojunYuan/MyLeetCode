# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.process(root)[1]
    
    def process(self, node):
        # for any node, we have 2 possibilities
        # 1. max path will go through curr node
        # 2. max path does not go through curr node
        if not node:
            return 0, -math.inf
        left, leftmax = self.process(node.left)
        right, rightmax = self.process(node.right)
        
        local = max(max(left,right) + node.val, 0)
        localmax = max(leftmax, rightmax, left + right + node.val)
        
        return local, localmax