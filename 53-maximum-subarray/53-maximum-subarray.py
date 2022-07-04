class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res,tempMax=nums[0],0
        for num in nums:
            tempMax=max(tempMax+num,num)
            res=max(res,tempMax)
        return res