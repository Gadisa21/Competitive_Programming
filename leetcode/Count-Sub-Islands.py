class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        dir=[(1,0),(-1,0),(0,1),(0,-1)]
        
        def inbound(row,col):
            return 0<=row<len(grid1) and 0<=col<len(grid1[0])
        
        visited=set()
        def dfs(r,c):
            if grid2[r][c]==0:
                return True
            visited.add((r,c))

            res=True

            if grid1[r][c]==0:
                res=False
            for x,y in dir:
                if inbound(r+x,y+c) and (r+x,y+c) not in visited:
                    res=dfs(r+x,y+c) and res
            return res
        count=0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):

                if grid2[i][j]!=0 and (i,j) not in visited and dfs(i,j):
                    count+=1
        return count



            
