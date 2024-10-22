class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # stack
        profit = 0
        stack = []
        for p in prices:
            if stack and p > stack[-1]:
                profit += p - stack.pop()
            stack.append(p)
        return profit