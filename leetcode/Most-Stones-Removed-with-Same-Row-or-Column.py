class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent={i:i for i in range(len(stones))}

        # map_num={nums:i for i, nums in enumerate(stones)}


        graph=defaultdict(list)

        rank=[1]*len(stones)
        
        for i,nums in enumerate(stones):
            x,y=nums

            for j in range(i+1,len(stones)):
                x2,y2=stones[j]

                if x==x2 or y2==y:
                    graph[i].append(j)
        
        def find(x):
            if x==parent[x]:
                return x
            parent[x]=find(parent[x])
            
            return parent[x]
        
        def union(x,y):
            pX=find(x)
            pY=find(y)

            if pX!=pY:

                if rank[pX]>rank[pY]:
                    parent[pY]=pX
                elif rank[pY]>rank[pX]:
                    parent[pX]=pY
                else:
                    parent[pY]=pX
                    rank[pX]+=1
        for key,values in graph.items():

            for val in values:
                union(key,val)
        
        coun=0

        for i in range(len(stones)):
            if i==find(i):
                coun+=1
        
        return len(stones)-coun

        

        
        