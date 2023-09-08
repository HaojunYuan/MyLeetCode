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
        if root is None:
            return None
        
        # recursive case
        # flatten left subtree
        self.flatten(root.left)
        # flatten right subtree
        self.flatten(root.right)
        
        # store right subtree
        right_subtree = root.right
        
        # move left subtree to right
        root.right = root.left
        root.left = None
        
        # find the end of the new right subtree
        while root.right:
            root = root.right
        
        # append the right subtree
        root.right = right_subtree
        