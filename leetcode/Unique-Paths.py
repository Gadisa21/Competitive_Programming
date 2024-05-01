class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo=[[0]*n for i in range(m)]

        def inbound(i,j):
            return 0<=i<m and 0<=j<n

        def dp(i,j):
            if i==m-1 and j==n-1:
                return 1
            
            if memo[i][j]==0:
                
                if inbound(i,j+1):
                    memo[i][j]+=dp(i,j+1)
                if inbound(i+1,j):
                    memo[i][j]+=dp(i+1,j)
            return memo[i][j]
        return dp(0,0)

                
        