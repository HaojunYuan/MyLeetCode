class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # to make a valid tree, there cannot be circle
        # if two nodes with edge connecting them already belong to the same parent, then there is a circle and the tree is not valid
        # otherwise, the tree is valid
        # union find
        # there can only be 1 connected component without circle
        parent = [i for i in range(n)]
        degree = [1] * n
        components = n
        
        def find(p):
            while p!=parent[p]:
                p=parent[p]
            return p
        
        def union(n1,n2):
            p1,p2=find(n1), find(n2)
            if p1==p2:
                return 0
            
            # make the parent with smaller degree belong to the parent with larger degree
            
            if degree[p1]<degree[p2]:
                degree[p2]+=degree[p1]
                parent[p1]=p2
            else:
                degree[p1]+=degree[p2]
                parent[p2]=p1
            
            return 1
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return False
            components-=1
            
        return components ==1