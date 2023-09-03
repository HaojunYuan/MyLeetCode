class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        tmp = sorted(nums[x:])
        res = inf
        for i, n in enumerate(nums):
            if not tmp:
                break
            if n <= tmp[0]:
                res = min(tmp[0] - n, res)
            elif n >= tmp[-1]:
                res = min(n - tmp[-1], res)
            else:
                idx = bisect_left(tmp, n)
                res = min(min(abs(n - tmp[idx]), abs(n - tmp[idx-1])), res)
            tmp.pop(bisect_left(tmp, nums[i+x]))
        return res
