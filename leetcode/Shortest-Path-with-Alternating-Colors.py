class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_edge=defaultdict(list)
        blue_edge=defaultdict(list)

        for node1,node2 in redEdges:
            red_edge[node1].append(node2)
        
        for node1,node2 in blueEdges:
            blue_edge[node1].append(node2)
        visited=set()
        que=deque([(0,0,None)])
        answer=[-1 for i in range(n)]
        # visited.add((0,None))
        while que:
            node,length,color=que.popleft()
            if answer[node]==-1:
                answer[node]=length
            
            if color!="RED":
                for neighbour in red_edge[node]:
                    if (neighbour,"RED") not in visited:
                        visited.add((neighbour,"RED"))
                        que.append((neighbour,length+1,"RED"))

            if color!="BLUE":
                for neighbour in blue_edge[node]:
                    if (neighbour,"BLUE") not in visited:
                        visited.add((neighbour,"BLUE"))
                        que.append((neighbour,length+1,"BLUE"))

        return answer

        
        