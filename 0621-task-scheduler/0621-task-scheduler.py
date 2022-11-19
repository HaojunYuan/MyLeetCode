class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c=Counter(tasks)
        maxFreq=0
        maxCount=0
        for key,freq in c.items():
            if freq==maxFreq:
                maxCount+=1
            elif freq>maxFreq:
                maxFreq=freq
                maxCount=1
        
        intervals=maxFreq-1
        slots=intervals*(n-maxCount+1)
        idle=max(0,slots-(len(tasks)-maxFreq*maxCount))
        res=len(tasks)+idle
        return res
        