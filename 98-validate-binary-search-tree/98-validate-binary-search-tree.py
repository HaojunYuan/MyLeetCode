# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node,low=-math.inf,high=math.inf):
            if not node:
                return True
            elif node.val<=low or node.val>=high:
                return False
            else:
                return helper(node.left,low,node.val) and helper(node.right,node.val,high)
        
        return helper(root)
            