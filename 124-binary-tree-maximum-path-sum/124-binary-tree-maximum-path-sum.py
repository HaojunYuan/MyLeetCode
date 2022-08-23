# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum=-math.inf
        def maxGain(node):
            nonlocal maxSum
            if not node:
                return 0
            
            leftGain=max(maxGain(node.left),0)
            rightGain=max(maxGain(node.right),0)
            
            currSum=node.val+leftGain+rightGain
            maxSum=max(maxSum,currSum)
            
            return node.val+max(leftGain,rightGain)
            
        maxGain(root)
        return maxSum
            