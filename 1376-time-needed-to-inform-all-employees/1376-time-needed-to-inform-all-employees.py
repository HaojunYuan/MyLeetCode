class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subs=defaultdict(list)
        self.res=0
        for i,m in enumerate(manager):
            subs[m].append(i)
        
        # bfs
        q=deque([(headID,0)])
        while q:
            m,time=q.popleft()
            self.res=max(self.res,time)
            for s in subs[m]:
                q.append((s,time + informTime[m]))
        return self.res