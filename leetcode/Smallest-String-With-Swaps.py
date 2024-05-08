class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def dfs(node):
            visited.add(node)
            component.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        graph = defaultdict(list)
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        result = list(s)
        
        for i in range(len(s)):
            if i not in visited:
                component = []
                dfs(i)
                indices = sorted(component)
                chars = sorted(result[idx] for idx in component)
                for idx, char in zip(indices, chars):
                    result[idx] = char
        
        return ''.join(result)
