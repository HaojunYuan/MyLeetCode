class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l <= r:
            h = min(height[l], height[r])
            width = r - l
            res = max(res, h * width)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res