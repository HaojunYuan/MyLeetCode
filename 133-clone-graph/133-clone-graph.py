"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #DFS
        clone={}
        def helper(node):
            if not node:
                return node
            elif node in clone:
                return clone[node]
            
            #we have a node that is not in the clone
            #create a copy for the node and put it in the clone
            cloneNode=Node(node.val,[])
            clone[node]=cloneNode
            cloneNode.neighbors=[helper(n) for n in node.neighbors]
            return cloneNode
        return helper(node)
    
        # #BFS
        # if not node:
        #     return node
        # clone={}
        # dq=deque([node])
        # while dq:
        #     temp=dq.popleft()
        #     if temp not in clone:
        #         clone[temp]=Node(temp.val,[])
        #     for n in temp.neighbors:
        #         if n not in clone:
        #             clone[n]=Node(n.val,[])
        #             dq.append(n)
        #         clone[temp].neighbors.append(clone[n])
        # return clone[node]