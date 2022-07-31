class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums,i,j):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
            
        left=curr=0
        right=len(nums)-1
        
        while curr<=right:
            if nums[curr]==0:
                swap(nums,curr,left)
                left+=1
                curr+=1
            elif nums[curr]==2:
                swap(nums,curr,right)
                right-=1
            else:
                curr+=1

        
        return nums
                