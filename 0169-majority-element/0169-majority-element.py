class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # one pass
        major = None
        count = 0
        for n in nums:
            if count == 0:
                major = n
            count += 1 if n == major else -1
        return major
            