class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = nums[0]
        left = [n for n in nums if n < pivot]
        mid = [n for n in nums if n == pivot]
        right = [n for n in nums if n > pivot]
        
        if len(right) + len(mid) < k:
            return self.findKthLargest(left, k - len(right) - len(mid))
        elif len(right) >= k:
            return self.findKthLargest(right, k)
        else:
            return pivot