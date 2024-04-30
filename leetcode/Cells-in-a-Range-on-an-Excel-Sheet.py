class Solution:
    def cellsInRange(self, s: str) -> List[str]:

        s=s.split(":")
        row_start,row_end= int(s[0][-1]),int(s[-1][-1])
        col_start,col_end=s[0][0],s[-1][0]
        ans=[]
        for i in range(ord(col_start),ord(col_end)+1):
            for j in range(row_start,row_end+1):
                ans.append(chr(i)+str(j))

        
        return ans
        