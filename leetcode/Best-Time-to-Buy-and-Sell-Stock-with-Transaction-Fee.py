class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        memo=defaultdict(int)

        def dp(i,buying):

            if i>=len(prices):
                return 0
            
            

            if (i,buying) not in memo:
                exclude=dp(i+1,buying)
                if buying:
                    memo[(i,buying)]=max(exclude,dp(i+1,not buying)-prices[i])
                else:
                    memo[(i,buying)]=max(exclude,dp(i+1,not buying)+prices[i]-fee)
            return memo[(i,buying)]
        return dp(0,True)
        