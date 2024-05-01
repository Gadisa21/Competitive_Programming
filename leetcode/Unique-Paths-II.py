class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j]==1:
                    obstacleGrid[i][j]=-1
        

        def inbound(i,j):
            return 0<=i<len(obstacleGrid) and 0<=j<len(obstacleGrid[0])
        if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]==0:
            obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]=1
        else:
            obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]=0
        for i in range(len(obstacleGrid)-1,-1,-1):
            for j in range(len(obstacleGrid[0])-1,-1,-1):
                if inbound(i,j+1) and obstacleGrid[i][j]!=-1 and obstacleGrid[i][j+1]!=-1 :
                    obstacleGrid[i][j]+=obstacleGrid[i][j+1]
                if inbound(i+1,j) and obstacleGrid[i+1][j]!=-1 and obstacleGrid[i][j]!=-1:
                    obstacleGrid[i][j]+=obstacleGrid[i+1][j]
        return obstacleGrid[0][0] if obstacleGrid[0][0] !=-1 else 0
        