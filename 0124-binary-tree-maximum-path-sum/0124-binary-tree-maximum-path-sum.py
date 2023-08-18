# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The path may or may not pass through the root
        
class Info:
    def __init__(self, partial, total):
        self.partial=partial
        self.total=total
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.process(root).total
    def process(self, node):
        if not node:
            return Info(0,-math.inf)
        left=self.process(node.left)
        right=self.process(node.right)
        left.partial=max(left.partial, 0)
        right.partial=max(right.partial, 0)
        
        partial=node.val+max(left.partial, right.partial)
        total=max(left.total, right.total, left.partial+right.partial+node.val)
        return Info(partial, total)