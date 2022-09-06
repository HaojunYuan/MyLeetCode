class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic=defaultdict(list)
        indegree=[0]*numCourses
        for child, parent in prerequisites:
            dic[parent].append(child)
            indegree[child]+=1
        
        dq=deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                dq.append(i)
        
        res=[]
        while dq:
            course=dq.popleft()
            res.append(course)
            for child in dic[course]:
                indegree[child]-=1
                if indegree[child]==0:
                    dq.append(child)
        
        return res if len(res)==numCourses else []
        