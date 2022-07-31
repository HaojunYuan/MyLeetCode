"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def __init__(self):
        self.clone={}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        if node in self.clone:
            return self.clone[node]
        
        cloneNode=Node(node.val,[])
        self.clone[node]=cloneNode
        
        cloneNode.neighbors=[self.cloneGraph(i) for i in node.neighbors]
        
        return cloneNode
        