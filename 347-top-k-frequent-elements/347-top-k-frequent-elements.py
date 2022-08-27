class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        freqList=[[] for _ in range(len(nums)+1)]
        for num,freq in counter.items():
            freqList[freq].append(num)
        res=[]
        for i in range(len(freqList)-1,-1,-1):
            for num in freqList[i]:
                res.append(num)
        return res[:k]