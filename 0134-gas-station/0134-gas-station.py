class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        # find the starting point. When we iterate through the gas stations, gas in tank cannot fall below 0. Otherwise, we start from the next gas station
        start = 0
        total = 0
        gasInTank = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1
        return start
