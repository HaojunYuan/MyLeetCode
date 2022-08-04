class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree=[0]*numCourses
        res=[]
        dic={i:[] for i in range(numCourses)}
        
        for child, parent in prerequisites:
            inDegree[child]+=1
            dic[parent].append(child)
        
        
        dq=deque()
        for i in range(numCourses):
            if inDegree[i]==0:
                dq.append(i)
        
        count=0
        while dq:
            curr=dq.popleft()
            res.append(curr)
            count+=1
            for child in dic[curr]:
                inDegree[child]-=1
                if inDegree[child]==0:
                    dq.append(child)
                    
        return res if count==numCourses else []