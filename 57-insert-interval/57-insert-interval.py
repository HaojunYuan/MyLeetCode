class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left,right=[],[]
        start,end=newInterval[0],newInterval[1]
        for i in intervals:
            if i[1]<start:
                left.append(i)
            elif i[0]>end:
                right.append(i)
            else:
                start=min(i[0],start)
                end=max(i[1],end)
                
        return left+[[start,end]]+right