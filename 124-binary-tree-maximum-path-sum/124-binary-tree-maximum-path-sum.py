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
        def maxGain(node):
            if not node:
                return 0
            leftGain=max(0,maxGain(node.left))
            rightGain=max(0,maxGain(node.right))
            self.maxSum=max(self.maxSum,node.val+leftGain+rightGain)
            return node.val+max(leftGain,rightGain)
        maxGain(root)
        return self.maxSum