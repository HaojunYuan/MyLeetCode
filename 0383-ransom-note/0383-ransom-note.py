class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        dic=collections.Counter(magazine)
        for char in ransomNote:
            if dic[char]==0:
                return False
            else:
                dic[char]=dic[char]-1
        return True