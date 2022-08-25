# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getDepth(root):
            if not root:
                return 0
            return 1+max(getDepth(root.left),getDepth(root.right))
        if not root:
            return True
        
        return abs(getDepth(root.left)-getDepth(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)