class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            tempsum=0
            temp=i
            while temp!=0:
                tempsum+=temp%2
                temp=temp//2
            res.append(tempsum)
        return res