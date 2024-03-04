class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = maxPrice = prices[0]
        for price in prices:
            # Signal to sell
            if price < maxPrice:
                maxProfit += maxPrice - minPrice
                minPrice = maxPrice = price
            else:
                minPrice = min(minPrice, price)
                maxPrice = price
        maxProfit += maxPrice - minPrice
        return maxProfit