class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # initialize dp array to be all 1, since all element itself is a subsequence
        # iterate through nums with index
        # for each index, iterate through all prior elements. Increment the index by dp[j] if nums[j] is smaller than nums[i]
        # update result, since the maximum subsequence might not be at the end, so we have to update the result every time we checked a subsequence
        n = len(nums)
        dp = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)