"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        clone={}
        if not node:
            return node
        dq=deque([node])
        clone[node]=Node(node.val,[])
        
        while dq:
            curr=dq.popleft()
            for n in curr.neighbors:
                if n not in clone:
                    clone[n]=Node(n.val,[])
                    dq.append(n)
                clone[curr].neighbors.append(clone[n])
        
        return clone[node]