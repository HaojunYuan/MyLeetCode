class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        pattern=defaultdict(list)
        for user, time, web in sorted(zip(username, timestamp, website)):
            pattern[user].append(web)
            
        counter = Counter()
        for user, path in pattern.items():
            # Since the score is the number of users x that visited the pattern, a user who visited one pattern multiple times only contribut to 1 score. So we need to use set to prevent duplicates.
            for triple in set(itertools.combinations(path, 3)):
                counter[triple]+=1
        
        res=None
        maxCount=0
        for pat, count in counter.items():
            if count>maxCount:
                res=pat
                maxCount=count
            elif count==maxCount and pat<res:
                res=pat
        return res