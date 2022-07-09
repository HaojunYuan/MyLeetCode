class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic=collections.Counter(nums)
        for num in dic:
            if dic[num]>len(nums)//2:
                return num