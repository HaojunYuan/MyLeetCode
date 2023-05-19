class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        # the minimum in the array is where nums[i]<nums[i-1], then nums[i] is the minimum
        # after we have the middle point, we compare it with nums[0] to determine our current location in the nums array and how we move the left and right pointers
        l,r=0,len(nums)-1
        if nums[l]<=nums[r]:
            return nums[l]
        while l<=r:
            mid=l+(r-l)//2
            if mid-1>=0 and nums[mid]<nums[mid-1]:
                return nums[mid]
            elif mid+1<len(nums) and nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[mid]>nums[l]:
                l=mid+1
            else:
                r=mid-1
            