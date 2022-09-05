# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(node):
            if not node:
                return 0
            else:
                return 1+max(getHeight(node.left),getHeight(node.right))
        if not root:
            return True
        return abs(getHeight(root.left)-getHeight(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)