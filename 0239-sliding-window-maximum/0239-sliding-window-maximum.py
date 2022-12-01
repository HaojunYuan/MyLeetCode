class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k==0:
            return nums
        dq=deque()
        res=[]
        for i in range(len(nums)):
            if dq and i-dq[0]==k:
                dq.popleft()
            while dq and nums[i]>nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i>=k-1:
                res.append(nums[dq[0]])
            
        return res
                
                