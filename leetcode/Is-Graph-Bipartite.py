class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        color=[-1 for i in range(len(graph))]
        visited=set()
        def dfs(node):
            temp=True
            for neighbour in graph[node]:
                if color[neighbour]==-1:
                    if color[node]==1:
                        color[neighbour]=0
                        temp=temp and dfs(neighbour)
                        return temp
                    else:
                        color[neighbour]=1
                        temp=temp and dfs(neighbour)
                else:
                    temp=temp and color[neighbour]!=color[node]
            return temp
        result=True
        for i in range(len(graph)):
            if color[i]==-1:
                color[i]=0
                result=result and dfs(i)

        return result


                    
                        



        