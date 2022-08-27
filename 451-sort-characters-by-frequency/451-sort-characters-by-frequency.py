class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return s
        counter=collections.Counter(s)
        maxFreq=max(counter.values())
        buckets=[[] for _ in range(maxFreq+1)]
        
        for char, freq in counter.items():
            buckets[freq].append(char)
        
        string=[]
        for i in range(len(buckets)-1,-1,-1):
            for char in buckets[i]:
                string.append(char*i)
        return ''.join(string)
                