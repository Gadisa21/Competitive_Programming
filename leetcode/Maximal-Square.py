class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        def inbound(r,c):
            if 0<=r<len(matrix) and 0<=c <len(matrix[0]):
                return int(matrix[r][c])
            else:
                return 0
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                if matrix[i][j]!="0":
                    right=inbound(i,j+1)
                    bottom=inbound(i+1,j)
                    diag=inbound(i+1,j+1)
                    matrix[i][j]= 1+min(right,bottom,diag)
                else:
                    matrix[i][j]=0
        res=0
        for i in range(len(matrix)):
            res=max(res,max(matrix[i]))
        return res**2

                    
        