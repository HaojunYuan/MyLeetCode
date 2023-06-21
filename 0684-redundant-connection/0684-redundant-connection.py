class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union find
        # if two nodes have the same parent, they are alr connected and the connection is redundant
        
        parent = [i for i in range(len(edges))]
        degree = [1]*len(edges)
        res=[]
        
        def find(p):
            while p!=parent[p]:
                p=parent[p]
            return p
        
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return 1
            elif degree[p1]>degree[p2]:
                degree[p1]+=degree[p2]
                parent[p2]=p1
            else:
                degree[p2]+=degree[p1]
                parent[p1]=p2
            return 0
        for n1, n2 in edges:
            if union(n1-1,n2-1):
                res=[n1,n2]
        return res