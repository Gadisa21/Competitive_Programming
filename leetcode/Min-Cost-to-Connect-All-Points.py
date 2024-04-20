class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        possible_edges={i:[] for i in range(len(points))}

        for i in range(len(points)):
            x1,y1=points[i]
            for j in range(i+1,len(points)):
                x2,y2=points[j]
                possible_edges[i].append([abs(x1-x2)+abs(y1-y2),j])
                possible_edges[j].append([abs(x1-x2)+abs(y1-y2),i])
        
        visited=set()
        minHeap=[[0,0]]
        result=0

        while len(visited)<len(points):

            cost,node=heapq.heappop(minHeap)

            if node in visited:
                continue
            visited.add(node)

            result+=cost

            for newC,v in possible_edges[node]:
                if v not in visited:
                    heapq.heappush(minHeap,[newC,v])
        return result
            

        