import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.indexMap = {}

    def insert(self, val: int) -> bool:
        if val not in self.indexMap:
            self.nums.append(val)
            self.indexMap[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.indexMap:
            # To remove the val in O(1), swap the value with the last value in the nums array, then pop from the array
            index = self.indexMap[val]
            lastNum = self.nums[-1]
            self.nums[index], self.indexMap[lastNum] = lastNum, index
            self.nums.pop()
            self.indexMap.pop(val, 0)
            return True
        return False

    def getRandom(self) -> int:
        return self.nums[random.randint(0,len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()