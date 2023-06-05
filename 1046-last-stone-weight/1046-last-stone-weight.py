class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # need to invert stones since we want to pop the largest weights
        for i in range(len(stones)):
            stones[i]*=-1
        heapq.heapify(stones)
        # at most 1 stone will left
        while len(stones)>1:
            first=heapq.heappop(stones)
            second=heapq.heappop(stones)
            if second!=first:
                heapq.heappush(stones,first-second)
        return -stones[0] if stones else 0
        