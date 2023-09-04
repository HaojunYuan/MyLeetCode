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
    def verticalOrderBFS(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Use a hashmap to store col - node indexing
        if not root:
            return
        q = deque([[root,0]])
        while q:
            node, col = q.popleft()
            if col not in self.hashMap:
                self.hashMap[col] = []
            self.hashMap[col].append(node.val)
            self.small = min(self.small, col)
            self.large = max(self.large, col)
            if node.left:
                q.append([node.left,col - 1])
            if node.right:
                q.append([node.right,col + 1])
                
        
        return [self.hashMap[i] for i in range(self.small, self.large + 1)]
    
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        self.process(root, 0, 0)
        res = []
        for i in range(self.small, self.large + 1):
            values = self.hashMap[i]
            values.sort(key = lambda x: x[1])
            level = []
            for value in values:
                level.append(value[0])
            res.append(level)
        return res
            
    def process(self, node, row, col):
        if not node:
            return
        
        if col not in self.hashMap:
            self.hashMap[col] = []
        self.hashMap[col].append([node.val, row])
        self.small = min(self.small, col)
        self.large = max(self.large, col)
        self.process(node.left, row + 1, col - 1)
        self.process(node.right, row + 1, col + 1)