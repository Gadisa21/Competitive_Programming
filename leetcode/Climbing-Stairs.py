class Solution:
    def climbStairs(self, n: int) -> int:

        memo=defaultdict(int)

        def rc(no):
            if no==1:
                return 1
            if no==2:
                return 2
            
            if no not in memo:
                memo[no]=rc(no-1)+rc(no-2)
            return memo[no]
        return rc(n)
                

        