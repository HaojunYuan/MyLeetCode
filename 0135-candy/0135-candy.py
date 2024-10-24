class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0
        
        # Step 1: Initialize candies array, each child gets at least 1 candy
        candies = [1] * n
        
        # Step 2: Left to right traversal to ensure higher ratings get more candies than left neighbor
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
                
        # Step 3: Right to left traversal to ensure higher ratings get more candies than right neighbor
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        # Step 4: The result is the total number of candies
        return sum(candies)
