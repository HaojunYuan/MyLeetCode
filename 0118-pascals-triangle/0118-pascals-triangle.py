class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1]]
        if numRows < 3:
            return res[:numRows]
        prev = [1, 1]
        for r in range(3, numRows + 1):
            curr = [1]
            for i in range(r - 2):
                curr.append(prev[i] + prev[i + 1])
            curr.append(1)
            res.append(curr)
            prev = curr
        return res
        
        