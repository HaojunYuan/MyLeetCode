class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # because the maximum product might come from multiplication of two negative numbers, we need to choose between 3 products: negMax*n, posMax*n and n
        Min,Max = 1,1
        res=nums[0]
        for n in nums:
            temp=Max
            Max=max(Max*n,Min*n,n)
            Min=min(temp*n, Min*n, n)
            res=max(res,Max)
        return res