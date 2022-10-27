class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dep=defaultdict(list)
        visited=[False]*len(accounts)
        res=[]
        
        for i,account in enumerate(accounts):
            for j in range(1,len(account)):
                dep[account[j]].append(i)
        
        def helper(i,emails):
            if visited[i]:
                return
            visited[i]=True
            for j in range(1,len(accounts[i])):
                email=accounts[i][j]
                emails.add(email)
                for user in dep[email]:
                    helper(user,emails)
        
        for i,account in enumerate(accounts):
            if visited[i]:
                continue
            name,emails=account[0],set()
            helper(i,emails)
            res.append([name]+sorted(emails))
    
        return res
                
                
        