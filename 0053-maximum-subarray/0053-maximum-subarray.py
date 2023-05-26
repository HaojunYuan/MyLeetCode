class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if the temporary sum is negative, we discard it, since adding negative number to any existing number will only make it smaller not larger
        res=-math.inf
        temp=0
        for n in nums:
            temp+=n
            res=max(res,temp)
            temp=max(temp,0)
        return res