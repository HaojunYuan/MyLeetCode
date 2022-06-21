class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l=len(nums)
        i=1
        while i<l:
            if nums[i]>0 and nums[i]<l and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
            else:
                i+=1
        for i in range(l):
            if nums[i]!=i+1:
                return i+1
        return l+1