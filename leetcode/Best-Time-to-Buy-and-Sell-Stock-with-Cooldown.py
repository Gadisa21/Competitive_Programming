class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo=defaultdict(int)

        def dp(i,buying):

            if i>=len(prices):
                return 0
            
            cooldown=dp(i+1,buying)

            if (i,buying) not in memo:
                if buying:
                    memo[(i,buying)]=max(cooldown,dp(i+1,not buying)-prices[i]) 
                else:
                    memo[(i,buying)]=max(cooldown,dp(i+2,not buying)+ prices[i]) 
            return memo[(i,buying)]
        return dp(0,True)
