class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic={}
        res,dup=set(),set()
        for i,num1 in enumerate(nums):
            if num1 not in dup:
                dup.add(num1)
                for j,num2 in enumerate(nums[i+1:]):
                    comp=-num1-num2
                    if comp in dic and dic[comp]==i:
                        res.add(tuple(sorted((num1,num2,comp))))
                    dic[num2]=i
        return res