class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        in_degree=defaultdict(int)
        graph=defaultdict(list)
        supplies=set(supplies)

        for i,recip in enumerate(recipes):
            for ingredient in ingredients[i]:
                if ingredient not in supplies:
                    graph[ingredient].append(recip)
                    in_degree[recip]+=1
                    
        que=deque()
        
        for recip in recipes:
            if in_degree[recip]==0:
                que.append(recip)
        
        ans=[]

        while que:
            recip=que.popleft()

            for re in graph[recip] :
                in_degree[re]-=1

                if in_degree[re]==0:
                    que.append(re)
            ans.append(recip)
        return ans

        