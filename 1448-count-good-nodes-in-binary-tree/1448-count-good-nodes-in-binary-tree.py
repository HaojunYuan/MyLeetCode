# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res=0
        def isGood(currMax,node):
            if not node:
                return
            if currMax<=node.val:
                self.res+=1
            currMax=max(currMax,node.val)
            isGood(currMax,node.left)
            isGood(currMax,node.right)
        isGood(root.val,root)
        return self.res