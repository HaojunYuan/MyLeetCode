class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic=defaultdict(list)
        indegree=[0]*numCourses
        
        for child, parent in prerequisites:
            indegree[child]+=1
            dic[parent].append(child)
        
        dq=deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                dq.append(i)
        
        res=[]
        while dq:
            temp=dq.popleft()
            res.append(temp)
            for child in dic[temp]:
                indegree[child]-=1
                if indegree[child]==0:
                    dq.append(child)
        return len(res)==numCourses