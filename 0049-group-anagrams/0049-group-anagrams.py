class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for s in strs:
            if tuple(sorted(s)) not in dic:
                dic[tuple(sorted(s))]=[]
            dic[tuple(sorted(s))].append(s)
        return dic.values()