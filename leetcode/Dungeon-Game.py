class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        dp=[[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]

        def inbound(i,j):
            return 0<=i<len(dungeon) and 0<=j<len(dungeon[0])
        if dungeon[-1][-1]<0:
            dp[-1][-1]=-dungeon[-1][-1]
        else:
            dp[-1][-1]=0
        for i in range(len(dungeon)-1,-1,-1):
            for j in range(len(dungeon[0])-1,-1,-1):
                if i==len(dungeon)-1 and len(dungeon[0])-1==j:
                    continue
                min_health=float("inf")

                if inbound(i,j+1):
                    min_health=dp[i][j+1]
                if inbound(i+1,j):
                    min_health=min(min_health,dp[i+1][j])
                if dungeon[i][j]<0:
                    dp[i][j]=min_health-dungeon[i][j]
                else:
                    if dungeon[i][j]>=min_health:
                        dp[i][j]=0
                    else:
                        dp[i][j]=min_health-dungeon[i][j]
        return dp[0][0] +1 




        