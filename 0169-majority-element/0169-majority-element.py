class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        major = nums[0]
        for n in nums:
            if n == major:
                c += 1
            else:
                c -= 1
                if c < 0:
                    major = n
                    c = 1
        return major