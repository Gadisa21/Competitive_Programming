class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo=[[-1]*len(text1) for i in range(len(text2))]
      
        def dp(i,j):
            if i>=len(text2) or j>=len(text1):
                return 0

            if memo[i][j]==-1:
                include=0
                if text1[j]==text2[i]:
                    include=1+dp(i+1,j+1)
                exclude=max(dp(i,j+1),dp(i+1,j))

                memo[i][j]=max(include,exclude)
            return memo[i][j]
        return dp(0,0)


        