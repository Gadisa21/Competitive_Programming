class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo=defaultdict(int)

        def dp(cs,i):
            if cs==0:
                return 1
            if cs<0 or i>=len(coins):
                return 0
            
            if (cs,i) not in memo:
                memo[(cs,i)]=dp(cs-coins[i],i) + dp(cs,i+1)
            return memo[(cs,i)]

            
        return dp(amount,0)
            
        