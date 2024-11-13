class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        posMax = negMax = 1
        res = nums[0]
        for n in nums:
            temp = posMax
            posMax = max(n, posMax * n, negMax * n)
            negMax = min(n, temp * n, negMax * n)
            res = max(res, posMax, negMax)
        return res