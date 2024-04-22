class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        parent={}
        for letter in string.ascii_lowercase:
            parent[letter]=letter
        
        def find(x):

            if x==parent[x]:
                return x
            parent[x]=find(parent[x])

            return parent[x]
        def union(x,y):
            parentX=find(x)
            parentY=find(y)

            if parentX!=parentY:
                if parentX>parentY:
                    parent[parentX]=parentY
                else:
                    parent[parentY]=parentX
        
        for i in range(len(s1)):
            union(s1[i],s2[i])
        
        ans=""

        for i in range(len(baseStr)):
            ans+=find(baseStr[i])
        
        return ans
        

        