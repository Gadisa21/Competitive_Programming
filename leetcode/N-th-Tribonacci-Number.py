class Solution:
    def tribonacci(self, n: int) -> int:
        
        memo={}
        def dp(no):
            if no==0:
                return 0
            if no<=2:
                return 1
            if no not in memo:
                memo[no]=dp(no-3)+dp(no-2)+dp(no-1)
            return memo[no]
        return dp(n)

