class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c=Counter(words)
        
        buckets=[[] for _ in range(len(words)+1)]
        
        for word, freq in c.items():
            buckets[freq].append(word)
        
        res=[]
        for i in range(len(buckets)-1,-1,-1):
            bucket=buckets[i]
            for word in sorted(bucket):
                res.append(word)
        
        return res[:k]