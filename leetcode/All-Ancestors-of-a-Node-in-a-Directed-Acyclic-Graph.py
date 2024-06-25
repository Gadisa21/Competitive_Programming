class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph=defaultdict(list)

        in_degree=defaultdict(int)

        for u,v in edges:
            graph[u].append(v)
            in_degree[v]+=1
        result=[set()]*n
        que=deque()
        for i in range(n):
            if in_degree[i]==0:
                que.append(i)
       
        
        while que:
            node=que.popleft()

            for neigh in graph[node]:
                result[neigh]= result[neigh] | result[node]
                result[neigh].add(node)
                in_degree[neigh]-=1
                if in_degree[neigh]==0:
                    que.append(neigh)
        
        for i in range(n):
            result[i]=sorted(list(result[i]))

        return result

                


        