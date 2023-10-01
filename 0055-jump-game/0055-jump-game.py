class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0  # Initialize the maximum reachable position.

        for i in range(n):
            # If the current position is unreachable, return False.
            if i > max_reach:
                return False
            
            # Update the maximum reachable position.
            max_reach = max(max_reach, i + nums[i])

            # If we can reach the end, return True.
            if max_reach >= n - 1:
                return True
        
        return True  # If we reach here, we can reach the end.

# Usage:
# sol = Solution()
# result = sol.canJump([2, 3, 1, 1, 4])
# print(result)  # Output: True
