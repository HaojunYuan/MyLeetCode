class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # union find
        # a list to store the parent for each node. A node is its own parent
        parent=[i for i in range(n)]
        # degree of each node
        degree=[1]*n
        components=n
        
        # find the starting parent of the node
        def find(node):
            while node!=parent[node]:
                node=parent[node]
            return node
        
        # union two nodes based on their parent's degree
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            # if they alr have the same parent, return False
            if p1==p2:
                return 0
            if degree[p1]<degree[p2]:
                # make p2 p1's parent
                parent[p1]=p2
                degree[p2]+=degree[p1]
            else:
                parent[p2]=p1
                degree[p1]+=degree[p2]
            return 1
        
        for n1,n2 in edges:
            components-=union(n1,n2)
        return components