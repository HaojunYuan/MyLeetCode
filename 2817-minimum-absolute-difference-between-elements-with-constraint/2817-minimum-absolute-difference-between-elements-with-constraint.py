from sortedcontainers import SortedSet

class Solution:

    

    def minAbsoluteDifference(self, nums, x):
        ans = float('inf')
        s = SortedSet()

        for i in range(x, len(nums)):
            s.add(nums[i - x])

            it = s.bisect_left(nums[i])

            if it != len(s):
                ans = min(ans, abs(nums[i] - s[it]))

            if it != 0:
                ans = min(ans, abs(nums[i] - s[it - 1]))

        return ans

