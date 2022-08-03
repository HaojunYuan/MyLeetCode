class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter=collections.Counter()
        for domain in cpdomains:
            count,domain=domain.split()
            count=int(count)
            subDomains=domain.split('.')
            for i in range(len(subDomains)):
                counter['.'.join(subDomains[i:])]+=count
        
        return [' '.join((str(a),b)) for b,a in counter.items() ]