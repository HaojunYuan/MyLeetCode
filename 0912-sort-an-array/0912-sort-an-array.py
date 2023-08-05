class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l, r=0, len(nums)-1
        res=self.process(l,r,nums)
        return res
    
    def process(self, l, r, arr):
        if l>=r:
            return [arr[l]]
        mid=l+(r-l)//2
        left=self.process(l,mid,arr)
        right=self.process(mid+1, r, arr)
        res=self.merge(left, right)
        return res
    
    def merge(self, left, right):
        temp=[]
        i=0
        j=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                temp.append(left[i])
                i+=1
            else:
                temp.append(right[j])
                j+=1
        
        while i<len(left):
            temp.append(left[i])
            i+=1
        while j<len(right):
            temp.append(right[j])
            j+=1
        return temp