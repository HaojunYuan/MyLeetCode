class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use sorted str as key
        dic = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in dic:
                dic[key] = []
            dic[key].append(s)
        return dic.values()