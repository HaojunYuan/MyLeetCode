class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        posMax, negMax = 1, 1
        res = nums[0]
        for n in nums:
            temp = posMax
            posMax = max(posMax * n, negMax * n, n)
            negMax = min(temp * n, negMax * n, n)
            res = max(posMax, negMax, res)
        return res