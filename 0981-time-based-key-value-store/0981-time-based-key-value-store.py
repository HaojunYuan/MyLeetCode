class TimeMap:

    def __init__(self):
        self.dic=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dic:
            record=self.dic[key]
            l,r=0,len(record)-1
            if record[l][1]>timestamp:
                return ""
            elif record[r][1]<=timestamp:
                return record[r][0]
            else:
                while l<=r:
                    mid=l+(r-l)//2
                    if record[mid][1]==timestamp:
                        return record[mid][0]
                    elif record[mid][1]<timestamp:
                        l=mid+1
                    else:
                        r=mid-1
                return record[r][0]
        return ""
                


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)