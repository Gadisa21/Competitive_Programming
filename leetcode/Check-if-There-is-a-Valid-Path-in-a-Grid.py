class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        visited=set()
        direction={
            1:[(0,-1),(0,1)],
            2:[(-1,0),(1,0)],
            3:[(0,-1),(1,0)],
            4:[(0,1),(1,0)],
            5:[(-1,0),(0,-1)],
            6:[(0,1),(-1,0)]
        }
        def inbound(row,col):
            return (0<=row<len(grid)) and (0<=col<len(grid[0]))

        def dfs(row,col):
            if row==len(grid)-1 and col==len(grid[0])-1:
                return True
            
            visited.add((row,col))
            for x,y in direction[grid[row][col]]:
                new_row=x+row
                new_col=y+col
                if inbound(new_row,new_col) and (new_row,new_col) not in visited and (-x,-y) in direction[grid[new_row][new_col]]:
                    found=dfs(new_row,new_col)
                    if found:
                        return True
            return False
        return dfs(0,0)
        