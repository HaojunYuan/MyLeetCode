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
        
        self.clone[node]=Node(node.val,[])
        self.clone[node].neighbors=[self.cloneGraph(n) for n in node.neighbors]
        return self.clone[node]
    
#         clone={}
#         if not node:
#             return node
#         dq=deque([node])
#         clone[node]=Node(node.val,[])
        
#         while dq:
#             temp=dq.popleft()
#             for n in temp.neighbors:
#                 if n not in clone:
#                     clone[n]=Node(n.val,[])
#                     dq.append(n)
#                 clone[temp].neighbors.append(clone[n])
#         return clone[node]