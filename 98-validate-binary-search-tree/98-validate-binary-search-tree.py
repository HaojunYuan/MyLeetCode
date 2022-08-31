# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node,left=-math.inf,right=math.inf):
            if not node:
                return True
            elif node.val<=left or node.val>=right:
                return False
            else:
                return helper(node.left,left,node.val) and helper(node.right,node.val,right)
        return helper(root)