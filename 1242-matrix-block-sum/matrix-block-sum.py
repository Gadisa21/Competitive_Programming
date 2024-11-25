class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        prefix = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                prefix[i][j] = mat[i][j]
                if i > 0:
                    prefix[i][j] += prefix[i-1][j]
                if j > 0:
                    prefix[i][j] += prefix[i][j-1]
                if i > 0 and j > 0:
                    prefix[i][j] -= prefix[i-1][j-1]
        
        answer = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                r1, c1 = max(0, i-k), max(0, j-k)
                r2, c2 = min(m-1, i+k), min(n-1, j+k)
                
                block_sum = prefix[r2][c2]
                if r1 > 0:
                    block_sum -= prefix[r1-1][c2]
                if c1 > 0:
                    block_sum -= prefix[r2][c1-1]
                if r1 > 0 and c1 > 0:
                    block_sum += prefix[r1-1][c1-1]
                
                answer[i][j] = block_sum
        
        return answer