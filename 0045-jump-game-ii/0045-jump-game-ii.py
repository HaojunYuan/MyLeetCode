class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0  # If there's only one element, no jumps are needed.

        max_reach = nums[0]  # Maximum reachable position in the current jump.
        steps = 1  # Number of jumps taken so far.
        current_max_reach = nums[0]  # Maximum reachable position in the next jump.

        for i in range(1, n):
            if i > max_reach:
                # We need to take a jump because we cannot reach the current position.
                steps += 1
                max_reach = current_max_reach

            # Update the maximum reachable position for the next jump.
            current_max_reach = max(current_max_reach, i + nums[i])

        return steps