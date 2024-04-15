class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        que=deque()
        time,fresh=0,0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    que.append([i,j])
        
        def inbound(row,col):
            return (0<=row<len(grid)) and (0<=col<len(grid[0]))
        while que and fresh>0:
            for i in range(len(que)):
                r,c=que.popleft()
                for x,y in direction:
                    new_row=x+r
                    new_col=y+c
                    if inbound(new_row,new_col) and grid[new_row][new_col]==1:
                        grid[new_row][new_col]=2
                        fresh-=1
                        que.append([new_row,new_col])
            time+=1
        return time if fresh==0 else -1



        