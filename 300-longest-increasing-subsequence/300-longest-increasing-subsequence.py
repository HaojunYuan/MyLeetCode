class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binarysearch(sub,val):
            lo=0
            hi=len(sub)-1
            while lo<=hi:
                mid=lo+(hi-lo)//2
                if sub[mid]==val:
                    return mid
                elif sub[mid]<val:
                    lo=mid+1
                else:
                    hi=mid-1
            return lo
        
        sub=[]
        for num in nums:
            index=binarysearch(sub,num)
            if index==len(sub):
                sub.append(num)
            else:
                sub[index]=num
        return len(sub)