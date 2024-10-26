class Solution:
    def intToRoman(self, num: int) -> str:
        # List of Roman numerals and their integer values
        val_to_symbol = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        result = ""
        
        # Convert the integer to Roman numeral by matching values from highest to lowest
        for value, symbol in val_to_symbol:
            while num >= value:
                result += symbol
                num -= value
        
        return result
