# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxSum=-math.inf

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxSum(node):
            if not node:
                return 0
            left=max(0,maxSum(node.left))
            right=max(0,maxSum(node.right))
            self.maxSum=max(self.maxSum,node.val+left+right)
            return node.val+max(left,right)
        maxSum(root)
        return self.maxSum
            
