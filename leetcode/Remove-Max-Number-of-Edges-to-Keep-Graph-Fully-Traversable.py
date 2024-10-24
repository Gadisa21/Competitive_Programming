class UnionFind:

    def __init__(self,n):
        self.parent={i:i for i in range(1,n+1)}
        self.rank=[0]*(n+1)

    def find(self,x):

        if x==self.parent[x]:
            return x
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        parentX=self.find(x)
        parentY=self.find(y)

        if parentX!=parentY:
            if self.rank[parentX]>self.rank[parentY]:
                self.parent[parentY]=parentX
            elif self.rank[parentX]<self.rank[parentY]:
                self.parent[parentX]=parentY
            else:
                self.parent[parentX]=parentY
                self.rank[parentY]+=1
        else:
            return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufA=UnionFind(n)
        ufB=UnionFind(n)
        rmvN=0

        for edge in edges:

            if edge[0] ==3:
                
                if ufA.union(edge[1],edge[2]):
                    rmvN+=1
                else:
                    ufB.union(edge[1],edge[2])
        for edge in edges:

            if edge[0]!=3:
                if edge[0]==1:
                    if ufA.union(edge[1],edge[2]):
                        rmvN+=1
                else:
                    if ufB.union(edge[1],edge[2]):
                        rmvN+=1
        rootA=ufA.find(1)
        rootB=ufB.find(1)
       

        for i  in range(1,n+1):

            if rootA!=ufA.find(i) or rootB!= ufB.find(i):
                return -1
            

        return rmvN
            

        