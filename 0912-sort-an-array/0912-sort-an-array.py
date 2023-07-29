class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort
        l, r = 0, len(nums) - 1
        self.process(l, r, nums)
        return nums
    
    def process(self, l, r, arr):
        # base case
        if l >= r:
            return
        mid = l + (r - l) // 2
        self.process(l, mid, arr)
        self.process(mid + 1, r, arr)
        self.merge(l, mid, r, arr)
    
    def merge(self, l, mid, r, arr):
        temp = []
        i, j = l, mid + 1
        while i <= mid and j <= r:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= r:
            temp.append(arr[j])
            j += 1
        
        for i in range(len(temp)):
            arr[l + i] = temp[i]
