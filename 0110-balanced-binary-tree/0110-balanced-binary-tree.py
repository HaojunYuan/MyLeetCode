# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Info:
    def __init__(self,height, isBalanced):
        self.height=height
        self.isBalanced=isBalanced
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.process(root).isBalanced
    def process(self, node):
        if not node:
            return Info(0, True)
        left=self.process(node.left)
        right=self.process(node.right)
        balance=abs(left.height-right.height)<=1 and left.isBalanced and right.isBalanced
        return Info(1+max(left.height, right.height), balance)
        