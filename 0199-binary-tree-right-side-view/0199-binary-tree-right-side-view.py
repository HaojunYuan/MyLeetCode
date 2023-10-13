# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        dq = deque([root])
        res = []
        while dq:
            level = []
            for _ in range(len(dq)):
                curr = dq.popleft()
                level.append(curr.val)
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
            res.append(level[-1])
        return res