class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # iterate through s with a start index
        # for j in range i, check if s[j:i+1] is palindrome
        # append to curr
        # dfs(i+1, curr)
        # curr.pop()
        
        res=[]
        def dfs(start, curr):
            if start==len(s):
                res.append(curr[:])
                return
            for i in range(start, len(s)):
                if self.isPalindrome(s,start, i):
                    curr.append(s[start:i+1])
                    dfs(i+1, curr)
                    curr.pop()
        dfs(0,[])
        return res
        
        
    def isPalindrome(self,s, l, r):
        while l<=r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True