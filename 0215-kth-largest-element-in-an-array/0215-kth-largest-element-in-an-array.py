class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot=nums[0]
        left=[n for n in nums if n<pivot]
        mid=[n for n in nums if n==pivot]
        right=[n for n in nums if n>pivot]
        
        if k<=len(right):
            return self.findKthLargest(right,k)
        elif k>len(mid)+len(right):
            return self.findKthLargest(left,k-len(mid)-len(right))
        else:
            return pivot