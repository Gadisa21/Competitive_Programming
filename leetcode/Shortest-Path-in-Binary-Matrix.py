class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direction=[(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]

        def inbound(row,col):
            return (0<=row<len(grid)) and (0<=col<len(grid[0]))
        
        que=deque()
        visited=set()
        if grid[0][0]==1:
            return -1
        que.append((0,0,1))
        visited.add((0,0))

        while que:
            row,col,length=que.popleft()
            if row==len(grid)-1 and col==len(grid)-1:
                return length

            for r,c in direction:
                new_row=r+row
                new_col=c+col
                if inbound(new_row,new_col) and (new_row,new_col) not in visited and grid[new_row][new_col]==0:
                    visited.add((new_row,new_col))
                    que.append((new_row,new_col,length+1))
        return -1
        