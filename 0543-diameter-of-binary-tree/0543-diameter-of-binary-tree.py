# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # depth of the left subtree + depth of the right subtree
        # if diameter>res, update
        # to ensure what we return to the root lead to maximum diameter, return the maximum depth of left or right subtree of each node
        self.res=0
        def helper(node):
            if not node:
                return 0
            left=helper(node.left)
            right=helper(node.right)
            self.res=max(self.res,left+right)
            return 1+max(left,right)
        helper(root)
        return self.res