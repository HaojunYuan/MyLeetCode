class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        l=len(nums)
        for i in range(l):
            if nums[i]>0:
                break
            elif i==0 or nums[i]!=nums[i-1]:
                comp=0-nums[i]
                left=i+1
                right=l-1
                while left<right:
                    if nums[left]+nums[right]==comp:
                        ans.append( [nums[i],nums[left],nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        left+=1
                        right-=1
                    elif nums[left]+nums[right]<comp:
                        left+=1
                    else:
                        right-=1
        return ans
                
                