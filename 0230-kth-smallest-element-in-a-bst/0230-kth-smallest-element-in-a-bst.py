# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order=[]
        self.helper(root,order)
        return order[k-1]
    
    def helper(self,node,order):
        if not node:
            return
        self.helper(node.left,order)
        order.append(node.val)
        self.helper(node.right,order)