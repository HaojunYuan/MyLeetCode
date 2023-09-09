class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])
        for r in box:
            switch_index = cols - 1
            for c in range(cols-1, -1, -1):
                if r[c] == '*':
                    switch_index = c - 1
                elif r[c] == '#':
                    r[c], r[switch_index] = r[switch_index], r[c]
                    switch_index -= 1
        
        # Rotate the image
        res = []
        for col in range(cols):
            temp = []
            for row in range(rows-1, -1, -1):
                temp.append(box[row][col])
            res.append(temp)
        return res
        
        
            