class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        memo={}

        def dp(l,r,turn):
            if l>r:
                return 0

            if (l,r,turn) not in memo:

                if  turn:
                    first_num=piles[l]+dp(l+1,r,not turn)
                    last_num=piles[r]+dp(l,r-1,not turn)
                    memo[(l,r,turn)]=max(last_num,first_num)
                else:
                    first_num=dp(l+1,r,not turn)
                    last_num=dp(l,r-1,not turn)
                    memo[(l,r,turn)]=max(last_num,first_num)
            return memo[(l,r,turn)]
        Alice=dp(0,len(piles)-1,True)
        if sum(piles)-Alice<Alice:
            return True
        else:
            return False




        