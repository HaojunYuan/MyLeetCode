class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res,dup=set(),set()
        seen={}
        for i, val1 in enumerate(nums):
            if val1 not in dup: #only continue if we have never seen this number before
                dup.add(val1)
                for j,val2 in enumerate(nums[i+1:]):
                    complement=-val1-val2
                    if complement in seen and seen[complement]==i: #only wen we have a complement for the current loop we can use the complement
                        res.add(tuple(sorted((val1, val2, complement))))
                        #sorted returns a list which is not hashable. Need to cast the list into a tuple so that we can put it into set
                    seen[val2]=i
        return res
                        