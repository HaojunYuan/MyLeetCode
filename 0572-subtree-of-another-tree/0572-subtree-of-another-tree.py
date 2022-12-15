# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def match(p,q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val!=q.val:
                return False
            
            return match(p.left,q.left) and match(p.right,q.right)
        
        if not root:
            return False
        if match(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)