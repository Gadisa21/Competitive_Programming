class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo=defaultdict(int)

        def dp(amount):
            if amount==0:
                return 1
            if amount<0:
                return 0
            if amount in memo:
                return memo[amount]
            comb=0

            for num in nums:
                comb+=dp(amount-num)
            memo[amount]=comb
            return memo[amount]
        return dp(target)
        