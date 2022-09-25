class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            tempsum=0
            # temp=i
            while i!=0:
                tempsum+=i%2
                i=i//2
            res.append(tempsum)
        return res