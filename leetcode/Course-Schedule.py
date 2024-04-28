class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph=defaultdict(list)

        for course,pre in prerequisites:
            graph[course].append(pre)
        
        visited=set()

        def dfs(crs):
            if graph[crs]==[]:
                return True
            if crs in visited:
                return False
            visited.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):return False
            visited.remove(crs)
            graph[crs]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):return False
        return True

        