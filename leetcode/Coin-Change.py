class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo=defaultdict(int)

        def dp(cs):

            if cs==0:
                return 0
            if cs<0:
                return float("inf")
            min_val=float("inf")
            for num in coins:
                if (num,cs) not in memo:
                    memo[(num,cs)]=1+dp(cs-num)
                min_val=min(min_val,memo[(num,cs)])
            return min_val
        ans=dp(amount)
        return ans if ans!=float("inf") else -1
                

        