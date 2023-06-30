class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        hasModified = False
        # 4,2,3
        # when we meet 4,2, we can either reduce the first number, or increase the second number
        # when we decrease the first number, we have to compare i-1 with i+1. If i-1<=i+1, then we reduce the first number
        # otherwise, we increase the second number
        for i in range(len(nums)):
            if i+1<len(nums) and nums[i]>nums[i+1]:
                if hasModified:
                    return False
                if i==0 or (i>0 and nums[i-1]<=nums[i+1]):
                    nums[i]=nums[i+1]
                else:
                    nums[i+1]=nums[i]
                hasModified = True
        return True
                    