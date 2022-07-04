class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res=tempMax=nums[0]
        for num in nums[1:]:
            tempMax=max(tempMax,0)+num
            res=max(res,tempMax)
        return res