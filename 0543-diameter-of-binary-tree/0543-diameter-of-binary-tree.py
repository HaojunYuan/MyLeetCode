# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0
        # for each node:
        # 1. update the diameter
        # 2. return the longest path it can extend from either left or right side
        def helper(node):
            if not node:
                return 0
            left,right=helper(node.left),helper(node.right)
            self.res=max(self.res,left+right)
            return 1+max(left,right)
        helper(root)
        return self.res
        