class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo=defaultdict(int)

        def dp(i,buy,limit):

            if i>=len(prices) or limit==2:
                return 0

            if (i,buy,limit) not in memo:

                if buy:
                   by=-prices[i] +dp(i+1,not buy,limit)
                   not_by=dp(i+1,buy,limit)
                   memo[(i,buy,limit)]=max(by,not_by)
                else:
                    sell=prices[i]+dp(i+1,not buy,limit+1)
                    not_sell=dp(i+1,buy,limit)
                    memo[(i,buy,limit)]=max(sell,not_sell)
            return memo[(i,buy,limit)]
        return dp(0,True,0)