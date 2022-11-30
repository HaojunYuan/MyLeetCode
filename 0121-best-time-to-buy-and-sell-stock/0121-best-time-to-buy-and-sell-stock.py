class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=math.inf
        maxProfit=0
        for p in prices:
            minPrice=min(p,minPrice)
            maxProfit=max(maxProfit,p-minPrice)
        return maxProfit