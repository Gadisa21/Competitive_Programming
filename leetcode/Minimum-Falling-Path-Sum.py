class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        def inbound(i,j):
            return 0<=i<len(matrix) and 0<=j<len(matrix[0])
        


        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                min_val=float("inf")
                if inbound(i+1,j):
                    min_val=matrix[i+1][j]
                if inbound(i+1,j-1):
                    min_val=min(min_val,matrix[i+1][j-1])
                if inbound(i+1,j+1):
                    min_val=min(min_val,matrix[i+1][j+1])
                if min_val!=float("inf"):
                    matrix[i][j]+=min_val
        return min(matrix[0]) 