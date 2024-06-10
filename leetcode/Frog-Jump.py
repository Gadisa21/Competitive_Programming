class Solution:
    def canCross(self, stones: List[int]) -> bool:

        pos_map=defaultdict(int)
        memo={}

        for i in range(len(stones)):
            pos_map[stones[i]]=i
        
        def dp(i,jump):
            
            if i>=len(stones):
                return False
            if stones[i]==stones[-1]:
                return True
            if (i,jump) in memo:
                return memo[(i,jump)]
            
            if pos_map[jump-1 + stones[i]]>i:
                if dp(pos_map[jump-1 + stones[i]],jump-1):
                    return True
            if pos_map[jump+1 + stones[i]]>i:
                if dp(pos_map[jump+1 + stones[i]],jump+1):
                    return True
            if pos_map[jump + stones[i]]>i:
                if dp(pos_map[jump + stones[i]],jump):
                    return True
            memo[(i,jump)]=False
            return memo[(i,jump)]
        return dp(1,1) if stones[1]==1 else False
            
        