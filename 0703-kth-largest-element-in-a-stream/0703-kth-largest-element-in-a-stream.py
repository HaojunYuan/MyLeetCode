class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap,self.k=nums,k
        heapq.heapify(self.heap)
        # we only need to keep the k largest elements so that self.heap[0] is the kth largest element
        while len(self.heap)>k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        # we cannot use heappushpop becasue if len(self.heap)<k we do not have to pop
        if len(self.heap)>self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)