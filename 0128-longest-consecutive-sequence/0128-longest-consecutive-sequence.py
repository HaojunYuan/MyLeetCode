class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        streak=0
        for n in nums:
            if n-1 not in nums:
                temp=n+1
                while temp in nums:
                    temp+=1
                streak=max(streak,temp-n)
        return streak