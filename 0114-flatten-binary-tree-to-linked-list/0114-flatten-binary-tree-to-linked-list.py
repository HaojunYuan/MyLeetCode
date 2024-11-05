# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.process(root)
    
    def process(self, node):
        if not node:
            return 
        left = self.process(node.left)
        right = self.process(node.right)
        temp = right
        node.right = left
        node.left = None
        curr = node
        while curr.right:
            curr = curr.right
        curr.right = temp
        return node
        