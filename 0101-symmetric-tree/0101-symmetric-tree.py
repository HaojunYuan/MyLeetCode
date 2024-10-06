# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.process(root.left, root.right)
    
    def process(self, l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        return l.val == r.val and self.process(l.left, r.right) and self.process(l.right, r.left)