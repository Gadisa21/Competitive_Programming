class Solution:
    def integerBreak(self, n: int) -> int:

        memo=defaultdict(int)

        def dp(cs):

            if cs==0:
                return 1
            if cs<0:
                return float("-inf")
            
            if cs not in memo:
                for i in range(1,n):
                    memo[cs]=max(memo[cs],dp(cs-i)*i)
            return memo[cs]
        return dp(n)

        