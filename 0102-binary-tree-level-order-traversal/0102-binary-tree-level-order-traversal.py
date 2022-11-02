# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #dfs
        if not root:
            return root
        res=[]
        def dfs(node,level):
            if len(res)==level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                dfs(node.left,level+1)
            if node.right:
                dfs(node.right,level+1)
        dfs(root,0)
        return res
        # #bfs
        # if not root:
        #     return root
        # res=[]
        # dq=deque([root])
        # while dq:
        #     level=[]
        #     for _ in range(len(dq)):
        #         node=dq.popleft()
        #         level.append(node.val)
        #         if node.left:
        #             dq.append(node.left)
        #         if node.right:
        #             dq.append(node.right)
        #     res.append(level)
        # return res