class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree=[0]*numCourses
        dic={i:[] for i in range(numCourses)}
        res=[]
        
        for child,parent in prerequisites:
            indegree[child]+=1
            dic[parent].append(child)
        
        dq=deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                dq.append(i)
        
        while dq:
            parent=dq.popleft()
            res.append(parent)
            for child in dic[parent]:
                indegree[child]-=1
                if indegree[child]==0:
                    dq.append(child)
                    
        return res if len(res)==numCourses else []
        