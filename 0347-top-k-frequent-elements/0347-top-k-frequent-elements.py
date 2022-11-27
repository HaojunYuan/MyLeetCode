class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucketsort
        counter=Counter(nums)
        buckets=[[] for _ in range(len(nums)+1)]
        for num,freq in counter.items():
            buckets[freq].append(num)
        res=[]
        for bucket in buckets:
            for num in bucket:
                res.append(num)
        return res[::-1][:k]