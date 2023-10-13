# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.process(root, res)
        return res
    
    def process(self, node, res):
        if not node:
            return
        self.process(node.left, res)
        res.append(node.val)
        self.process(node.right, res)