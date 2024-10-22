class UnionFind:
    
    def __init__(self,n):
        self.parent={i:i for i in range(n)}
        self.rank=[0]*n
    
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
                self.parent[parentY]=parentX
                self.rank[parentX]+=1

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        uf=UnionFind(len(strs))

        def compare(index1,index2):
            diff=0

            for i in range(len(strs[index1])):
                if strs[index1][i]!=strs[index2][i]:
                    diff+=1
                if diff>2:
                    return
            uf.union(index1,index2)
        for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                compare(i,j)

        
        for i in range(len(strs)):
            uf.find(i)
        no_groups=len(set(uf.parent.values()))
      
        return no_groups
        