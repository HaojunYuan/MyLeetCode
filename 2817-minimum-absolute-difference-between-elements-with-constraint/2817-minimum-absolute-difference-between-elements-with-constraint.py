class Solution:
    def minAbsoluteDifference(self, nums: List[int], k: int) -> int:
        nums=sorted((val,idx) for idx,val in enumerate(nums))         
        stack1, stack2, res =[], [], float('inf')  

        for val,idx in nums:
            heappush(stack1,(k+idx,val)) 
            heappush(stack2,(k-idx,val))

            while stack1 and stack1[0][0]<=idx:                
                 res=min(res, val-heappop(stack1)[1])             
            while stack2 and stack2[0][0]<=-idx:                
                 res=min(res, val-heappop(stack2)[1])      

        return res
