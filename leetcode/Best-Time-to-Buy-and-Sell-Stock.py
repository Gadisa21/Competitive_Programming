class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        sell=prices[0]
        val=0

        for i in range(len(prices)):

            if sell<prices[i]:
                val=max(val,prices[i]-sell)
            if sell>prices[i]:
                sell=prices[i]
        return val
        