class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_count = {0: 1}  # Initialize with prefix_sum = 0 occurring once

        for num in nums:
            prefix_sum += num  # Update the cumulative sum
            # Check if there is a prefix_sum that makes the subarray sum to k
            if prefix_sum - k in prefix_count:
                count += prefix_count[prefix_sum - k]

            # Update the hash map with the current prefix_sum
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return count
