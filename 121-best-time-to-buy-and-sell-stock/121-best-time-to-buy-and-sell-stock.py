class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=math.inf
        maxprofit=0
        for price in prices:
            low=min(low,price)
            maxprofit=max(maxprofit,price-low)
        return maxprofit
        