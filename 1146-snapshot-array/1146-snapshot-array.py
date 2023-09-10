class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        self.indexHistory = [[[0,0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.indexHistory[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        history = self.indexHistory[index]
        l, r = 0, len(history) - 1
        res = 0
        while l <= r:
            mid = l + (r - l) // 2
            snapId, val = history[mid]
            if snapId <= snap_id:
                res = val
                l = mid + 1
            else:
                r = mid - 1
        return res

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)