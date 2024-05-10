class Solution:
    def reverseVowels(self, s: str) -> str:
        hash_map={"a","e","i","o","u","A","E","I","O","U"}

        p1,p2=0,len(s)-1
        ans=[""]*len(s)
        while p1<=p2:
            if s[p1] in hash_map and s[p2] in hash_map:
                ans[p1]=s[p2]
                ans[p2]=s[p1]
                p1+=1
                p2-=1
            else:
                if s[p1] in hash_map:
                    ans[p2]=s[p2]
                    p2-=1
                elif s[p2] in hash_map:
                    ans[p1]=s[p1]
                    p1+=1
                else:

                    ans[p1]=s[p1]
                    ans[p2]=s[p2]
                    p1+=1
                    p2-=1
            
        return "".join(ans)
        