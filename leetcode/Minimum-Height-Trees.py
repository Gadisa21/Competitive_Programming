class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]

        graph=defaultdict(list)

        edge_count=defaultdict(int)

        for u, v in edges:
            graph[u].append(v)
            edge_count[u]+=1
            graph[v].append(u)
            edge_count[v]+=1

        que=deque()
        for i in range(n):
            if edge_count[i]==1:
                que.append(i)
        while que:

            if n <=2:
                return list(que)
            for i in range(len(que)):
                node=que.popleft()

                for neigh in graph[node]:
                    edge_count[neigh]-=1
                    if edge_count[neigh]==1:
                        que.append(neigh)
                n-=1


        