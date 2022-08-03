class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter=collections.Counter()
        for d in cpdomains:
            count,domain=d.split()
            count=int(count)
            frags=domain.split('.')
            for i in range(len(frags)):
                counter['.'.join(frags[i:])]+=count
        
        return [' '.join((str(c),k)) for k,c in counter.items()]