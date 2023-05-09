class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # union find
        # Each node is the parent of itself
        parent=[i for i in range(n)]
        # Each node has an initial degree of 1
        degree=[1]*n
        # Number of components
        components=n
        
        # Find the parent of a node
        def find(p):
            while p!=parent[p]:
                p=parent[p]
            return p
        
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2: # Same parent already
                return 0
            else:
                if degree[p1]>degree[p2]:
                    # Make p1 the parent of p2
                    parent[p2]=p1
                    degree[p1]+=degree[p2]
                else:
                    parent[p1]=p2
                    degree[p2]+=degree[p1]
            return 1
        
        for n1,n2 in edges:
            components-=union(n1,n2)
        return components