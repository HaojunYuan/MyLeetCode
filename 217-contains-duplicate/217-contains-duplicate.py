class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=set()
        for num in nums:
            if num in a:
                return True
            a.add(num)
        return False