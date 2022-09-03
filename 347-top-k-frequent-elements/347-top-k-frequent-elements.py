class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        bucket=[[] for i in range(len(nums)+1)]
        for num,freq in counter.items():
            bucket[freq].append(num)
        res=[]
        for l in bucket:
            for num in l:
                res.append(num)
        return res[::-1][:k]
        