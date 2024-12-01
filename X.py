class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        curr_gcd=0
        deck=Counter(deck)
        for value in deck.values():
            curr_gcd=gcd(curr_gcd,value)
        if curr_gcd>1:
            return True
        return False
        