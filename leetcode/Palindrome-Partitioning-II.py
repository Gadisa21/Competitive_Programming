class Solution:
    def minCut(self, s: str) -> int:

        isPalindrom=[[False]*len(s) for _ in range(len(s))]
        i=0
        while i<len(s):
            isPalindrom[i][i]=True

            l=i-1
            r=i+1
            while 0<=l and r<len(s) and s[l]==s[r]:
                isPalindrom[l][r]=True
                l-=1
                r+=1
            l=i
            r=i+1
            while 0<=l and r<len(s) and s[l]==s[r]:
                isPalindrom[l][r]=True
                l-=1
                r+=1
            i+=1
        cuts=[0]*len(s)

        for i in range(len(s)):
            if isPalindrom[0][i]:
                continue
            else:
                cuts[i]=float("inf")
                for j in range(i):

                    if isPalindrom[j+1][i]:
                        cuts[i]=min(cuts[i],1+cuts[j])
            
        
        return cuts[-1] 