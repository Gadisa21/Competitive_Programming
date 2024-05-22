class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        memo=defaultdict(int)

        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            
            min_val=float("inf")

            for k in range(i+1,j):
                min_val=min(min_val,values[i]*values[k]*values[j]+dp(i,k)+dp(k,j))
            if min_val==float("inf"):
                return 0
            memo[(i,j)]=min_val
            return memo[(i,j)]
        return dp(0,len(values)-1)