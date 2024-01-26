class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [math.inf] * len(nums)
        dp[len(nums) - 1] = 0
        for i in range(len(nums) - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    dp[i] = min(dp[i], 1 + dp[i + j])
        return dp[0]
        
#         res = self.process(0, nums)
#         return res
    
#     def process(self, start, nums):
#         if start == len(nums) - 1:
#             return 0
#         if start + nums[start] >= len(nums) - 1:
#             return 1
#         res = math.inf
#         for i in range(1, nums[start] + 1):
#             res = min(res, self.process(start + i, nums))
#         return 1 + res