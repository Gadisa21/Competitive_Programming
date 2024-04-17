class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        root=[i for i in range(len(edges)+1)]

        rank=[1 ]*(len(edges)+1)

        def find(x):
            if x==root[x]:
                return x
            root[x]=find(root[x])
            return root[x]

        def union(x,y):
            parentx=find(x)
            parenty=find(y)

            if parentx==parenty:
                return [x,y]
            else:
                if rank[parentx]>rank[parenty]:
                    root[parenty]=parentx
                elif rank[parenty]>rank[parentx]:
                    root[parentx]=parenty
                else:
                    root[parentx]=parenty
                    rank[parenty]+=1
            return []
        for x ,y in edges:
            temp=union(x,y)
            if temp!=[]:
                return temp

        