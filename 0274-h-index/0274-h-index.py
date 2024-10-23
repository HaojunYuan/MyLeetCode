class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # counter
        n = len(citations)
        counter = [0] * (n + 1)
        for c in citations:
            if c >= n:
                counter[n] += 1
            else:
                counter[c] += 1
        
        i = n - 1
        while i >= 0:
            counter[i] += counter[i + 1]
            if counter[i + 1] >= i + 1:
                return i + 1
            i -= 1
        return 0