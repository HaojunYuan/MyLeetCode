# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.hashMap = {}
        self.small = 0
        self.large = 0
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Use a hashmap to store col - node indexing
        if not root:
            return
        q=[[root, 0]]
        while q:
            node, col = q.pop(0)
            if col not in self.hashMap:
                self.hashMap[col]=[]
            self.hashMap[col].append(node.val)
            self.small = min(self.small, col)
            self.large = max(self.large, col)
            if node.left:
                q.append([node.left,col-1])
            if node.right:
                q.append([node.right,col+1])
                
        
        return [self.hashMap[i] for i in range(self.small, self.large+1)]