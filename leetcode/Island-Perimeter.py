class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        direction=[(1,0),(-1,0),(0,1),(0,-1)]

        def inbound(row,col):
            return (0<=row<len(grid)) and (0<=col<len(grid[0]))
        
        ans=0
        visited=set()
        def dfs(row,col):
            if not inbound(row,col) or grid[row][col]==0:
                return 1
            if (row,col) in visited:
                return 0
            
            visited.add((row,col))
            temp=0
            for x,y in direction:
                new_row=x+row
                new_col=y+col
                if not (new_row,new_col) in visited:
                    temp+= dfs(new_row,new_col)
            return temp
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return dfs(i,j)
                    
        
        
            

        