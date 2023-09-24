class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = nums[-1]
        left = [n for n in nums if n < pivot]
        mid = [n for n in nums if n == pivot]
        right = [n for n in nums if n > pivot]
        
        # the largest element is in right
        if len(right) >= k:
            return self.findKthLargest(right, k)
        # in left
        elif len(right) + len(mid) < k:
            return self.findKthLargest(left, k - len(right) - len(mid))
        else:
            return mid[0]