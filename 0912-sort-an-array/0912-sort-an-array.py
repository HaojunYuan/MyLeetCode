class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l,r = 0, len(nums)-1
        self.process(nums, l, r)
        return nums
    
    def process(self, arr, l, r):
        if l>=r:
            return
        mid = l+(r-l)//2
        self.process(arr,l,mid)
        self.process(arr, mid+1, r)
        self.merge(arr, l, mid, r)
    
    def merge(self, arr,l, mid, r):
        temp=[]
        i, j = l, mid+1
        
        while i<=mid and j<=r:
            if arr[i]<=arr[j]:
                temp.append(arr[i])
                i+=1
            else:
                temp.append(arr[j])
                j+=1
        
        while i<=mid:
            temp.append(arr[i])
            i+=1
        while j<=r:
            temp.append(arr[j])
            j+=1
        
        # replace arr with temp
        for i in range(len(temp)):
            arr[l+i]=temp[i]