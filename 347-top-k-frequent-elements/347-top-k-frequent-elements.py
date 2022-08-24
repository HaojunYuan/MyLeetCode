class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        freqList=[[] for _ in range(len(nums)+1)]
        for num,freq in counter.items():
            freqList[freq].append(num)
        res=[]
        for l in freqList:
            for num in l:
                res.append(num)
        return res[::-1][:k]