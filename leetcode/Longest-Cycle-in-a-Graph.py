class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph=defaultdict(list)

        for node, neighbour in enumerate(edges):
            if neighbour!=-1:
                graph[node].append(neighbour)
        distance=defaultdict(int)
        visited=set()
        
        def dfs(node,currentD):
            if graph[node]==[] or distance[node]==-1:
                return -1
            
            if distance[node]!=0:
                start=distance[node]
                distance[node]=currentD
                value=distance[node]-start
                distance[node]=-1
                return value
            visited.add(node)
            distance[node]=currentD
            value=dfs(graph[node][0],currentD+1)
            distance[node]=-1
            return value
            
            

        
        longestC=-1
        for i in range(len(edges)):
            if i not in visited and edges[i]!=-1:
                longestC=max(dfs(i,0),longestC)
        print(visited)
        print(distance)
        return longestC



        