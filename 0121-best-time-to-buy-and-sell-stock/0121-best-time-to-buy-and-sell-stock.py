class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,minPrice=0,math.inf
        for price in prices:
            minPrice=min(price,minPrice)
            profit=max(profit,price-minPrice)
        return profit