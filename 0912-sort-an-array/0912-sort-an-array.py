class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        self.process(nums, l, r)
        return nums
    
    def process(self, nums, l, r):
        if l >= r:
            return
        mid = l + (r - l) // 2
        self.process(nums, l, mid)
        self.process(nums, mid + 1, r)
        self.merge(nums, l, mid, r)
    
    def merge(self, nums, l, mid, r):
        temp = []
        i = l
        j = mid + 1
        while i <= mid and j <= r:
            if nums[i] < nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= r:
            temp.append(nums[j])
            j += 1
            
        for i in range(len(temp)):
            nums[l + i] = temp[i]