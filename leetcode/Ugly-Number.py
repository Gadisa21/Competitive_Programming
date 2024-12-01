class Solution:
    def isUgly(self, n: int) -> bool:
        
        dic={2,3,5}


        d=2
        if n<=0:
            return False
        else:
            while d*d<=n:
                while n%d==0:
                    if d not in dic:
                        return False
                    n//=d
                d+=1
            if n>1:
                if n not in dic:
                    return False
            return True