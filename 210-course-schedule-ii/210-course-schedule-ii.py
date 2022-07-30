class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res=[]
        inDegree=[0]*numCourses
        dic={i:[] for i in range(numCourses)}
        
        for child,parent in prerequisites:
            dic[parent].append(child)
            inDegree[child]+=1
        
        
        dq=deque()
        for i in range(numCourses):
            if inDegree[i]==0:
                dq.append(i)
        
        count=0
        while dq:
            course=dq.popleft()
            res.append(course)
            count+=1
            for child in dic[course]:
                inDegree[child]-=1
                if inDegree[child]==0:
                    dq.append(child)
        
        return res if count==numCourses else []
                    