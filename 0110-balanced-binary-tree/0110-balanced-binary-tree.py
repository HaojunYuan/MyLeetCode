# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #For every node, the difference between the left subtree and right subtree cannot exceeds 1
        if not root:
            return True
        return abs(self.getDepth(root.left)-self.getDepth(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def getDepth(self,node):
        if not node:
            return 0
        return 1+max(self.getDepth(node.left), self.getDepth(node.right))