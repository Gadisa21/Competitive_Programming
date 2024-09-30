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
                self.parent[parentX]=parentY
                self.rank[parentY]+=1

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        uf=UnionFind(n)

        uf.union(0,firstPerson)

        meetings.sort(key=lambda x:x[-1])
        print(meetings)
        i=0
        secret=set()
        secret.add(0)
        secret.add(firstPerson)
        while i<len(meetings):
            temp=[]
            time=meetings[i][-1]
            while i<len(meetings) and time==meetings[i][-1]:
                temp.append(meetings[i])
                uf.union(meetings[i][0],meetings[i][1])
                i+=1
            for x,y,z in temp:
                if uf.find(x)!=uf.find(0):
                    uf.parent[x]=x
                    uf.rank[x]=0
                    uf.parent[y]=y
                    uf.rank[y]=0
                else:
                    if x not in secret:
                        secret.add(x)
                    
                    if y not in secret:
                        secret.add(y)
      
        return secret
                                
