# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution:
    def findClosestLeaf(self, root, k):
        # Time: O(n)
        # Space: O(n)
        
        graph, leaves = collections.defaultdict(list), set()
        
        def buildGraph(node):   # undirected
            if not node:
                return
            if not node.left and not node.right:
                leaves.add(node.val)
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                buildGraph(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                buildGraph(node.right)
        
        buildGraph(root)
        
        q = collections.deque([k])
        seen = set()
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                if cur in seen:
                    continue
                if cur in leaves:
                    return cur
                seen.add(cur)
                q+=graph[cur]
        
        
        
        
        
        
        
    
        