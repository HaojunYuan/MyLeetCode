class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If there's only one row or s is too short for zigzagging
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize rows for zigzag pattern
        rows = [""] * numRows
        current_row = 0
        going_down = False
        
        # Traverse the string and place each character in the correct row
        for char in s:
            rows[current_row] += char
            # Change direction if we reach the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move to the next row depending on the direction
            current_row += 1 if going_down else -1
        
        # Concatenate all rows to form the final result
        return "".join(rows)
