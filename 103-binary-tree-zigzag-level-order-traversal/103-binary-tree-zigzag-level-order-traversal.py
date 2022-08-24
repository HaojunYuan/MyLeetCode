# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        dq=deque([root])
        res=[]
        direction=1
        
        while dq:
            level=[]
            for _ in range(len(dq)):
                node=dq.popleft()
                level.append(node.val)
                if node.left: dq.append(node.left)
                if node.right:dq.append(node.right)
            res.append(level[::direction])
            direction*=-1
        return res