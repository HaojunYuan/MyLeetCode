class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # for each num[i]==num[i-1], continue the loop since we already considered it in the backtrack
        res=[]
        candidates.sort()
        
        def backtrack(start, curr, target):
            if target<0:
                return
            if target==0:
                res.append(curr[:])
                return
            
            # iterate through the candidates
            prev=-1
            for i in range(start, len(candidates)):
                if candidates[i]==prev:
                    continue
                curr.append(candidates[i])
                backtrack(i+1, curr, target-candidates[i])
                curr.pop()
                prev=candidates[i]
        
        backtrack(0,[],target)
        return res