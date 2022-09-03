class Solution:
    def findKthLargest(self, nums, k):
        if not nums: return
        pivot = random.choice(nums)
        left=[x for x in nums if x<pivot]
        mid=[x for x in nums if x==pivot]
        right=[x for x in nums if x>pivot]
        
        r,m=len(right),len(mid)
        if k<=r:
            return self.findKthLargest(right,k)
        elif k>r+m:
            return self.findKthLargest(left,k-r-m)
        else:
            return mid[0]
#         if not nums: return
#         pivot = random.choice(nums)
#         left =  [x for x in nums if x > pivot]
#         mid  =  [x for x in nums if x == pivot]
#         right = [x for x in nums if x < pivot]
        
#         L, M = len(left), len(mid)
        
#         if k <= L:
#             return self.findKthLargest(left, k)
#         elif k > L + M:
#             return self.findKthLargest(right, k - L - M)
#         else:
#             return mid[0]