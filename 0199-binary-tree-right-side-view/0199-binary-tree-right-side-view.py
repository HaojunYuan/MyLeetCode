# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        dq=deque([root])
        res=[]
        while dq:
            level=[]
            for _ in range(len(dq)):
                temp=dq.popleft()
                level.append(temp.val)
                if temp.left:
                    dq.append(temp.left)
                if temp.right:
                    dq.append(temp.right)
            res.append(level[-1])
        return res