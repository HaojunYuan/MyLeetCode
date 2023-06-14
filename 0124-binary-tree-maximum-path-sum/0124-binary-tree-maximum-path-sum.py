# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res=-math.inf # since there are negative numbers
        def helper(node):
            # get max sum from left and right subtree
            # update self.res
            # return max(left, right)
            if not node:
                return 0
            left=helper(node.left)
            right=helper(node.right)
            self.res=max(self.res,node.val+left+right)
            return max(node.val+max(left,right),0)
        helper(root)
        return self.res