class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree=defaultdict(int)
        outdegree=defaultdict(int)

        for x,y in trust:
            outdegree[x]+=1
            indegree[y]+=1

        for i in range(1,n+1):
            if indegree[i]==n-1 and not outdegree[i]:
                return i
        return -1
    
       
        