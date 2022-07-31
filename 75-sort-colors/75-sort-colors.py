class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums,i,j):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
            
        left=0
        
        for i in range(len(nums)):
            if nums[i]==0:
                swap(nums,i,left)
                left+=1
        
        right=len(nums)-1
        for j in range(len(nums)-1,-1,-1):
            if nums[j]==2:
                swap(nums,j,right)
                right-=1
        
        return nums
                