class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        memo=defaultdict(int)

        def dp(i,dayPass):
            if i>=len(days)  :
                return 0


            if (i,dayPass) not in memo:

                if dayPass>=days[i]:
                    memo[(i,dayPass)]=dp(i+1,dayPass)
                else:
                    memo[(i,dayPass)]=dp(i+1,days[i])+ costs[0]
                    memo[(i,dayPass)]=min(memo[(i,dayPass)],dp(i+1,days[i]+6)+costs[1])
                    memo[(i,dayPass)]=min(memo[(i,dayPass)],dp(i+1,days[i]+29)+costs[2])
            return memo[(i,dayPass)]
        return dp(0,0)



        