class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter=collections.Counter()
        for domain in cpdomains:
            count, domain=domain.split()
            count=int(count)
            frags = domain.split('.')
            for i in range(len(frags)):
                counter['.'.join(frags[i:])]+=count
        
        return [' '.join((str(v),k)) for k,v in counter.items()]