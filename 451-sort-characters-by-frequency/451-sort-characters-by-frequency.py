class Solution:
    def frequencySort(self, s: str) -> str:
        counter=Counter(s)
        bucket=[[] for _ in range(len(s)+1)]
        res=''
        
        for char, freq in counter.items():
            bucket[freq].append(char)
        
        for i in range(len(bucket)-1,-1,-1):
            for c in bucket[i]:
                res+=i*c
        return res