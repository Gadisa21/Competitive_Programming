class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=[[-1 for i in range( len(grid[0]))] for j in range(len(grid))]
        
        
        def inbound(row,col):
            return (0<=row<len(grid)) and (0<= col<len(grid[0]))
        
        def dfs(row,col):

            visited[row][col]=1

            for x,y in direction:
                new_row=row + x
                new_col=col + y

                if inbound(new_row,new_col) and visited[new_row][new_col]!=1 and grid[new_row][new_col]!="0":
                    dfs(new_row,new_col)
        

        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and visited[i][j]==-1:
                    dfs(i,j)
                    ans+=1
        return ans
                
                    
        

