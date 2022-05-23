class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=-math.inf
        pmax,nmax=1,1
        for num in nums:
            a=pmax*num
            b=nmax*num
            pmax=max(a,b,num)
            nmax=min(a,b,num)
            ans=max(pmax,ans)
        return ans
            