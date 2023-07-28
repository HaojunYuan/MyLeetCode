class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # decision tree dp
        dp={}
        # given index and current sum, how many ways can we reach the target        
        # we know at the end of the array if it is a way or not. If currSum==target, return 1 else 0
        def dfs(i, curr):
            if i==len(nums):
                return 1 if curr==target else 0
            if (i,curr) in dp:
                return dp[(i,curr)]
            
            # the number of ways to reach the target is the sum of adding the current index and minus the current index
            dp[(i, curr)] = dfs(i+1, curr+nums[i])+dfs(i+1, curr-nums[i])
            return dp[(i, curr)]
        return dfs(0,0)