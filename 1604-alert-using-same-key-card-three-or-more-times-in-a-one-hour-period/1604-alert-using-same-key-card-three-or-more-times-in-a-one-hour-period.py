class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        dic=collections.defaultdict(list)
        for name, time in zip(keyName,keyTime):
            hour,minute=time.split(':')
            hour,minute=int(hour),int(minute)
            totalMin=hour*60+minute
            dic[name].append(totalMin)
        res=[]
        for name,timeList in dic.items():
            timeList.sort()
            for i, time in enumerate(timeList):
                if i>=2 and time-timeList[i-2]<=60:
                    res.append(name)
                    break

                    
                    
        return sorted(res)