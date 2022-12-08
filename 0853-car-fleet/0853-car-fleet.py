class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time=[]
        for p,s in sorted(zip(position,speed)):
            time.append(float((target-p)/s))
        res=curr=0
        for t in time[::-1]:
            if t>curr:
                res+=1
                curr=t
        return res