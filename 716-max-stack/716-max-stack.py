class MaxStack(list):
    # def __init__(self):
    # self is a list of tuples: [(num,maxSoFar),(num,maxSoFar),(num,maxSoFar)...]
    def push(self, x: int) -> None:
        maxSoFar=max(x,self[-1][1] if self else -math.inf)
        self.append((x,maxSoFar))

    def pop(self) -> int:
        return list.pop(self)[0]

    def top(self) -> int:
        return self[-1][0]

    def peekMax(self) -> int:
        return self[-1][1]

    def popMax(self) -> int:
        maxSoFar=self[-1][1]
        popped=[]
        while self[-1][0]!=maxSoFar:
            popped.append(self.pop())
        
        #Now we find the most recent maximum number. Pop it off
        self.pop()
        #Use reversed for loop instead of map()
        for i in reversed(popped):
            self.push(i)
        return maxSoFar


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()