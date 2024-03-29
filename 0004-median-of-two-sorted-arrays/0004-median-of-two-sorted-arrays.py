class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=len(nums1)+len(nums2)
        if l%2:
            return self.kth(nums1,nums2,l//2)
        else:
            return (self.kth(nums1,nums2,l//2)+self.kth(nums1,nums2,l//2-1))/2
        
    def kth(self,a,b,k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia=len(a)//2
        ib=len(b)//2
        ma=a[ia]
        mb=b[ib]
        
        if ia+ib<k:
            if ma<mb:
                return self.kth(a[ia+1:],b,k-ia-1)
            else:
                return self.kth(a,b[ib+1:],k-ib-1)
        else:
            if ma<mb:
                return self.kth(a,b[:ib],k)
            else:
                return self.kth(a[:ia],b,k)
                
        