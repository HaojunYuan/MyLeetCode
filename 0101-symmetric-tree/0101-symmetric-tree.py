# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # reverse right tree
        # compare with left tree
        left, right = root.left, root.right
        right = self.reverse(right)
        return self.compare(left, right)
    
    def reverse(self, node):
        if not node:
            return None
        node.left, node.right = self.reverse(node.right), self.reverse(node.left)
        return node
    
    def compare(self, n1, n2):
        if not n1 and not n2:
            return True
        if not n1 or not n2:
            return False
        if n1.val != n2.val:
            return False
        return self.compare(n1.left, n2.left) and self.compare(n1.right, n2.right)
        