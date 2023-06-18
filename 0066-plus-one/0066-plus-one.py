class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        for i in range(len(digits)-1,-1,-1):
            if digits[i]==9 and carry:
                digits[i]=0
            else:
                digits[i]=digits[i]+carry
                carry=0
        # we might have a carry we need to prepend
        return digits if not carry else [carry]+digits
                