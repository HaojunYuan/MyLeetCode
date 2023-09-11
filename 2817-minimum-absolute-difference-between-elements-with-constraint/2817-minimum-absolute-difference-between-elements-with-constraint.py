class Solution:
    def minAbsoluteDifference(self, nums: List[int], k: int) -> int:
        nums = sorted((val, idx) for idx, val in enumerate(nums))         
        stack1, stack2, res = [], [], float('inf')  

        for val, idx in nums:
            # Push elements that are at most (k + idx) indices greater than the current index onto stack1
            # and elements that are at most (k - idx) indices less than the current index onto stack2.
            heappush(stack1, (k + idx, val)) 
            heappush(stack2, (k - idx, val))

            # Check and update the minimum absolute difference for stack1.
            while stack1 and stack1[0][0] <= idx:
                # Update res with the minimum absolute difference.
                res = min(res, val - heappop(stack1)[1])

            # Check and update the minimum absolute difference for stack2.
            while stack2 and stack2[0][0] <= -idx:
                # Update res with the minimum absolute difference.
                res = min(res, val - heappop(stack2)[1])

        return res

