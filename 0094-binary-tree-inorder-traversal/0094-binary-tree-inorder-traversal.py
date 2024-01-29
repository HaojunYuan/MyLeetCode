# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.process(root)
        return self.res
    
    def process(self, node):
        if not node:
            return
        self.process(node.left)
        self.res.append(node.val)
        self.process(node.right)