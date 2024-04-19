class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        parent={ i:i for i in range(1,n+1)}

        def find(x):
            if x==parent[x]:
                return x
            
            parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):

            pX=find(x)
            pY=find(y)

            if pX>pY:
                parent[pX]=pY
            else:
                parent[pY]=pX
        for v1,v2,c in roads:
            
            union(v1,v2)

        
        cost=float("inf")

        for v1,v2,c in roads:
            if find(v1)==1 and find(v2)==1:
                cost=min(cost,c)
        return cost

        