class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0):
            # if all integers are used up
            if first == n:  
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack (put the array back so that next iteration has the same array)
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output
        