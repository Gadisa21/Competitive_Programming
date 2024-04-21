class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        
        for rich, poor in richer:
            graph[poor].append(rich)
        
        ans = [None] * len(quiet)

        def dfs(node):
            if ans[node] is not None:
                return ans[node]
            
            ans[node] = node  
            for nei in graph[node]:
                candidate = dfs(nei)
                if quiet[candidate] < quiet[ans[node]]:
                    ans[node] = candidate
            return ans[node]

        for i in range(len(quiet)):
            if ans[i] is None:
                dfs(i)
        
        return ans
