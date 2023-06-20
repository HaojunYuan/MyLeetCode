class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # for each nums[i], we have two choices
        # to include all duplicates of nums[i]
        # do not include any nums[i]
        res=[]
        nums.sort()
        # sort the list to make sure duplicates are together
        def dfs(i,curr):
            # if we reach the end of the list, append the current path
            if i==len(nums):
                res.append(curr[:])
                return
            # all subsets that contain all duplicates of nums[i]
            curr.append(nums[i])
            dfs(i+1,curr)
            curr.pop()
            # all subsets that do not include any duplicates of nums[i]
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            # if all upcoming numbers are duplicate, i will reach the end of nums and just append the current path without any duplicate
            dfs(i+1,curr)
        dfs(0,[])
        return res