class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [math.inf] * len(nums)
        dp[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    dp[i] = min(dp[i], 1 + dp[i + j])
        return dp[0]
#         return self.process(0, nums)

#     def process(self, start, nums):
#         if start == len(nums) - 1:
#             return 0
#         elif start + nums[start] >= len(nums) - 1:
#             return 1
#         res = math.inf
#         for i in range(1, nums[start] + 1):
#             res = min(res, 1 + self.process(start + i, nums))
#         return res