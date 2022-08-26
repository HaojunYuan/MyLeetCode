class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        graph=defaultdict(list)
        for u, t, w in sorted(zip(username, timestamp, website)):
            graph[u].append(w)
        
        counter = Counter()
        for u, routes in graph.items():
            for triple in set(itertools.combinations(routes, 3)):
                counter[triple]+=1
        
        res=None
        maxCount=0
        for pat, count in counter.items():
            if count>maxCount:
                res=pat
                maxCount=count
            elif count==maxCount and pat<res:
                res=pat
        return res