class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # O(n^2logn)
        # dic={}
        # for s in strs:
        #     if tuple(sorted(s)) not in dic:
        #         dic[tuple(sorted(s))]=[]
        #     dic[tuple(sorted(s))].append(s)
        # return dic.values()
        
        # O(n^2)
        dic=collections.defaultdict(list)
        
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            dic[tuple(count)].append(s)
        return dic.values()