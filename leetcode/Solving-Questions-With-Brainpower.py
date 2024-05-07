class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        memo=defaultdict(int)

        def dp(indx):
            
            if indx>=len(questions):
                return 0
            
            if memo[indx]!=0:
                return memo[indx]
            solve=questions[indx][0] +dp(indx+questions[indx][1]+1)
            skip=dp(indx+1)
            memo[indx]=max(solve,skip)
            return memo[indx]
        return dp(0)
        