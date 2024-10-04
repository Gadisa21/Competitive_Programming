class Solution:
    def monkeyMove(self, n: int) -> int:

        def rec(base,exp,mod):
            if exp==0:
                return 1
            res=rec(base,exp//2,mod)
            total_res=(res*res)%mod

            if exp%2!=0:
                total_res=(total_res*base)%mod
            return total_res

        MOD=10**9 + 7
        ways=rec(2, n, MOD)
        return (ways-2)%MOD
        