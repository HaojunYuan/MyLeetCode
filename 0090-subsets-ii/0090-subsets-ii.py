class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # for each num in nums
        # 1. include all duplicates of num
        # 2. do not include any duplicate of num
        
        res=[]
        # sort the nums array so that duplicate numbers are next to each other
        nums.sort()
        def dfs(curr, i):
            if i==len(nums):
                res.append(curr[:])
                return
            # include all duplicates of nums[i]
            curr.append(nums[i])
            dfs(curr,i+1)
            curr.pop()
            # do not include any duplicate of nums[i]
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(curr,i+1)
        dfs([],0)
        return res