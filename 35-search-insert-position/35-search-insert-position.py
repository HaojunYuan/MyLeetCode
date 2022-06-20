# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         l,r=0,len(nums)-1
#         while l<=r:
#             mid=l+(r-l)>>1
#             if nums[mid]==target:
#                 return mid
#             elif nums[mid]<target:
#                 l=mid+1
#             else:
#                 r=mid-1
#         return l
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return left