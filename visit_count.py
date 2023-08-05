class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_count = {}
        
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            domain_parts = domain.split('.')
            
            for i in range(len(domain_parts)):
                subdomain = '.'.join(domain_parts[i:])
                domain_count[subdomain] = domain_count.get(subdomain, 0) + count
        
        result = []
        for subdomain, count in domain_count.items():
            result.append(str(count) + ' ' + subdomain)
        
        return result
