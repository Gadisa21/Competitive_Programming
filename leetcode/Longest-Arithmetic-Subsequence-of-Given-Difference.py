class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp=defaultdict(int)
        res=1
        for num in arr:
            res=max(res,1+dp[num-difference])
            dp[num]=1+dp[num-difference]
        return res