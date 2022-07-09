class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # dic=collections.Counter(nums)
        # for num in dic:
        #     if dic[num]>len(nums)//2:
        #         return num
        
        # Boyer-Moore Voting Algorithm
        count=0
        candidate=None
        
        for num in nums:
            if count==0:
                candidate=num
            count+=(1 if num==candidate else -1)
        return candidate