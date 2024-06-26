class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        parent={ i:i for i in range(len(accounts))}

        rank=[0]*len(accounts)

        def find(x):

            if x ==parent[x]:
                return x
            parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            pX=find(x)
            pY=find(y)

            if pX!=pY:
                if rank[pX]>rank[pY]:
                    parent[pX]=pY
                elif rank[pY]>rank[pX]:
                    parent[pY]=pX
                else:
                    parent[pX]=pY
                    rank[pY]+=1
        email_map={}

        for i,emails in enumerate(accounts):

            for em in emails[1:]:
                if em in email_map:
                    union(email_map[em],i)
                else:
                    email_map[em]=i
        
        email_account=defaultdict(list)
        for e,i in email_map.items():
            root=find(i)
            email_account[root].append(e)
        
        ans=[]
        for r,emails in email_account.items():
            ans.append([accounts[r][0]]+sorted(emails))
        return ans

            

        