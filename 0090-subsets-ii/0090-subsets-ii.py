class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # for each nums[i]
        # include all duplicates of nums[i]
        # do not include any duplicate of nums[i]
        res=[]
        nums.sort()
        def dfs(curr,i):
            if i==len(nums):
                res.append(curr[:])
                return
            # include all duplicates of nums[i]
            curr.append(nums[i])
            dfs(curr,i+1)
            curr.pop()
            
            # do not include any nums[i]
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(curr,i+1)
        
        dfs([],0)
        return res