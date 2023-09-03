class HitCounter:

    def __init__(self):
        self.times=[]

    def hit(self, timestamp: int) -> None:
        self.times.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        valid_times = [ts for ts in self.times if timestamp - ts<300]
        return len(valid_times)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)