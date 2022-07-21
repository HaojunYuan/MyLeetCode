class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        indegree=[0]*numCourses
        dic={i:[] for i in range(numCourses)}
        
        for child, parent in prerequisites:
            dic[parent].append(child)
            indegree[child]+=1
        
        dq=deque()
        
        for i in range(len(indegree)):
            if indegree[i]==0:
                dq.append(i)
                
        count=0
        while dq:
            course=dq.popleft()
            count+=1
            for child in dic[course]:
                indegree[child]-=1
                if indegree[child]==0:
                    dq.append(child)
        
        return count==numCourses
            