class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols=[False]*len(matrix[0])
        rows=[False]*len(matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    cols[j]=True
                    rows[i]=True
        for i in range(len(cols)):
            if cols[i]:
                for j in range(len(matrix)):
                    matrix[j][i]=0
        for i in range(len(rows)):
            if rows[i]:
                for j in range(len(matrix[0])):
                    matrix[i][j]=0
        