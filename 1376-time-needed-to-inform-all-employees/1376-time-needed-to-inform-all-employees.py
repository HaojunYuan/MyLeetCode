class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # the time is the maximum time needed to reach from root to a leaf node
        # time=time to reach the current node + informTime
        # build an manager-subordinate hashmap
        self.res=0
        dic=defaultdict(list)
        for i,m in enumerate(manager):
            dic[m].append(i)
        
        # bfs
        q=deque([(headID,0)])
        while q:
            m,time=q.popleft()
            self.res=max(self.res,time)
            for s in dic[m]:
                q.append((s,time+informTime[m]))
        return self.res
            