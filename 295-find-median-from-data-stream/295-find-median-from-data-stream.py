import heapq
class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]

    def addNum(self, num: int) -> None:
        heappush(self.small,-heappushpop(self.large,num))
        if len(self.small)>len(self.large):
            heappush(self.large,-heappop(self.small))

    def findMedian(self) -> float:
        if len(self.large)>len(self.small):
            return float(self.large[0])
        return (self.large[0]-self.small[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()