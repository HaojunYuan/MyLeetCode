class Solution:
    def frequencySort(self, s: str) -> str:
        counter=collections.Counter(s)
        bucket=[[] for _ in range(len(s)+1)]
        res=[]
        for char, freq in counter.items():
            bucket[freq].append(char)
            
        for i in range(len(bucket)-1,-1,-1):
            for c in bucket[i]:
                res.append(c*i)
        return ''.join(res)