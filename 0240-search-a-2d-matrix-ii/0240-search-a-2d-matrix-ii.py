class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in matrix:
            if self.binarySearch(r, target, 0, len(r) - 1):
                return True
        return False
    
    def binarySearch(self, arr, target, l, r):
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False