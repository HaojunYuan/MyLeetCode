class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c = defaultdict(list)
        for s in strs:
            c[tuple(sorted(list(s)))].append(s)
        return c.values()