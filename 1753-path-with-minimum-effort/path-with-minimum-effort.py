class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        col,row=len(heights[0]),len(heights)

        minHeap=[[0,0,0]]

        dr=[[0,1],[0,-1],[1,0],[-1,0]]
        visited=set()
        while minHeap:
            diff,r,c=heapq.heappop(minHeap)
            
            if (r,c) in visited:
                continue
            if (r,c)==(row-1,col-1):
                return diff
            visited.add((r,c))
            for x,y in dr:
                nx,ny=r+x,c+y
                if (nx<0 or ny<0 or nx==row or ny==col or (nx,ny) in visited):
                    continue
                newDiff=max(diff,abs(heights[nx][ny]-heights[r][c]))
                heapq.heappush(minHeap,[newDiff,nx,ny])
        