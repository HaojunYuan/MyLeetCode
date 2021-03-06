"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    #Recursive approach
    def __init__(self):
        self.visited={}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        
        clone=Node(node.val,[])
        self.visited[node]=clone
        
        clone.neighbors=[self.cloneGraph(n) for n in node.neighbors]
        
        return clone
    
    
#     #Iterative approach
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         visited={}
#         if not node:
#             return node
#         queue=deque([node])
#         visited[node]=Node(node.val,[])
        
#         while queue:
#             curr=queue.popleft()
#             for neighbor in curr.neighbors:
#                 if neighbor not in visited:
#                     visited[neighbor]=Node(neighbor.val,[])
#                     queue.append(neighbor)
#                 visited[curr].neighbors.append(visited[neighbor])
#         return visited[node]
                
            