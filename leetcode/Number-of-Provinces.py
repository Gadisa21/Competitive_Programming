class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        graph=defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]==1 and i!=j:
                    graph[i].append(j)
        
        visited=set()
        
        def dfs(node):

            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)
        ans=0
        for node in range(len(isConnected)):
            if node not in visited:
                dfs(node)
                ans+=1
        return ans

        