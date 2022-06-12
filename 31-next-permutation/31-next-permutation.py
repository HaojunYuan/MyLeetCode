class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=j=len(nums)-1
        while i>0 and nums[i-1]>=nums[i]:
            i-=1
        if i==0:
            nums.reverse()
            return
        a=i-1 #a is the first swapping index
        while nums[j]<=nums[a]:
            j-=1
        # now j is the second swapping index
        nums[a],nums[j]=nums[j],nums[a]
        l=a+1
        r=len(nums)-1
        while l<=r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1