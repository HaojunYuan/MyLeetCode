class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        c=Counter(nums)
        
        def dfs(curr):
            if len(curr)==len(nums):
                res.append(curr[:])
                return
            
            for n in c:
                if c[n] > 0:
                    curr.append(n)
                    c[n]-=1
                    
                    dfs(curr)
                    
                    c[n]+=1
                    curr.pop()
        dfs([])
        return res