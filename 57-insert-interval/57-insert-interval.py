# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         left,right=[],[]
#         start,end=newInterval[0],newInterval[1]
#         for i in intervals:
#             if i[1]<start:
#                 left+=i
#             elif i[0]>end:
#                 right+=i
#             else:
#                 start=min(i[0],start)
#                 end=max(i[1],end)
                
#         return [left]+[start,end]+[right]
class Solution:
    def insert(self, intervals, I):
        res, i = [], -1
        for i, (x, y) in enumerate(intervals):
            if y < I[0]:
                res.append([x, y])
            elif I[1] < x:
                i -= 1
                break
            else:
                I[0] = min(I[0], x)
                I[1] = max(I[1], y)
                
        return res + [I] + intervals[i+1:]