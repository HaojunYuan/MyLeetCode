# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def dfs(node):
            if not node:
                return 0
            l,r=dfs(node.left), dfs(node.right)
            #l+r is used to calculate maximum path
            self.res=max(self.res,l+r)
            #To form the maximum path, we need the path with maximum depth
            return 1+max(l,r)
        dfs(root)
        return self.res