class Solution:
    def monkeyMove(self, n: int) -> int:

        MOD=10**9 + 7
        ways=pow(2, n, MOD)
        return (ways-2)%MOD
        