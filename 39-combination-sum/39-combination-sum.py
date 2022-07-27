class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def helper(target,candidates,path,res):
            if target<0:
                return
            if target==0:
                res.append(path)
                return
            for i in range(len(candidates)):
                helper(target-candidates[i],candidates[i:],path+([candidates[i]]),res)
        
        helper(target,candidates,[],res)
        return res
            