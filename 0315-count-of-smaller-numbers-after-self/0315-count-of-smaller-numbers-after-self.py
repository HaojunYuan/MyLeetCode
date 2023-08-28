class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # since the index of the nums will change when we merge, use a list to keep track of indices when we merge sort the nums
        self.count=[0]*len(nums)
        self.indices = [i for i in range(len(nums))]
        l,r = 0,len(nums)-1
        self.process(l,r,nums)
        return self.count
    
    def process(self, l, r, nums):
        if l>=r:
            return
        mid = l+(r-l)//2
        self.process(l, mid, nums)
        self.process(mid+1, r, nums)
        self.merge(l,mid,r,nums)
    
    # We need to get info about smaller numbers after self when we merge
    def merge(self, l, mid, r, nums):
        # We sort the indices
        temp=[]
        i,j = l, mid+1
        while i<=mid and j<=r:
            if nums[self.indices[i]]<=nums[self.indices[j]]:
            # We need to update count because we know for nums[i] how many numbers on the right is smaller than nums[i]
                self.count[self.indices[i]]+=j-(mid+1)
                temp.append(self.indices[i])
                i+=1
            # nums[i]>nums[j]:
            else:
                temp.append(self.indices[j])
                j+=1
        while i<=mid:
            self.count[self.indices[i]]+=j-mid-1
            temp.append(self.indices[i])
            i+=1
        while j<=r:
            temp.append(self.indices[j])
            j+=1
        for i in range(len(temp)):
            self.indices[l+i]=temp[i]