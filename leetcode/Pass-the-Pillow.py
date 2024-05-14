class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        period=n-1
        turns=time//period
        rem=time%(n-1)

        if turns%2==0:
            return rem+1
        else:
            return n-rem

        