class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        if len(prerequisites)==0:
            return [False]*len(queries)
        
        graph=defaultdict(list)
        track=defaultdict(set)
        visited=set()

        for u,v in prerequisites:
            graph[u].append(v)
        
        def dfs(node):
            
            if graph[node]==[]:
                visited.add(node)
                return track[node]
            
            visited.add(node)

            for neigh in graph[node]:
                track[node].add(neigh)
                if neigh in visited:
                    track[node].update(track[neigh])
                else:
                    track[node].update(dfs(neigh))
            return track[node]
        
        

        for i in range(numCourses):
            if i in visited:
                continue
            else:
                dfs(i)
        ans=[]

        for u,v in queries:
            if v in track[u]:
                ans.append(True)
            else:
                ans.append(False)
        return ans







        
       
        
       