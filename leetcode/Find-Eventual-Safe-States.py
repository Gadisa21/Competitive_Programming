class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        safe={}
        ans=[]

        def dfs(node):
            if node in safe:
                return safe[node]
            safe[node]=False

            for nei in graph[node]:
                if not dfs(nei):
                    return False
            safe[node]=True
            return True

        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)
        return ans
        