class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.counts = [0] * len(nums)
        self.indices = list(range(len(nums))) # to keep track of indices
        self.mergeSort(nums, 0, len(nums) - 1)
        return self.counts
    
    def mergeSort(self, nums, l, r):
        if l >= r:
            return
        mid = l + (r - l) // 2
        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid + 1, r)
        self.merge(nums, l, mid, r)
    
    def merge(self, nums, l, mid, r):
        temp = [0] * (r - l + 1)
        i, j, k = l, mid + 1, 0

        while i <= mid and j <= r:
            if nums[self.indices[i]] <= nums[self.indices[j]]:
                temp[k] = self.indices[i]
                self.counts[self.indices[i]] += j - (mid + 1)
                i += 1
            else:
                temp[k] = self.indices[j]
                j += 1
            k += 1

        while i <= mid:
            temp[k] = self.indices[i]
            self.counts[self.indices[i]] += r - mid
            i += 1
            k += 1
        while j <= r:
            temp[k] = self.indices[j]
            k += 1
            j += 1
        
        for i in range(l, r + 1):
            self.indices[i] = temp[i - l]
