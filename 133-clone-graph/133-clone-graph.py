"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #dfs
        clone={}
        def helper(node):
            if not node:
                return node
            elif node in clone:
                return clone[node]
            clone[node]=Node(node.val,[])
            clone[node].neighbors=[helper(n) for n in node.neighbors]
            return clone[node]
        return helper(node)
        # #bfs
        # if not node:
        #     return node
        # dq=deque([node])
        # clone={}
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