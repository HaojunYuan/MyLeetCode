class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return nums
        deq, result = deque(), []
        for i in range(len(nums)):
            if i >= k:
                result.append(nums[deq[0]])   # save cur max from deque
                if deq[0] < i - k + 1:        # popleft item if left item leaves window
                    deq.popleft()
            while deq and nums[i] > nums[deq[-1]]:  # pop every smaller element from end
                deq.pop()
            deq.append(i)
        
        result.append(nums[deq[0]])
        return result