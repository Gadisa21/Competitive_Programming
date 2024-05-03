class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}


        def dp(cs,i):

            if (cs==target and i==len(nums) ) or i>=len(nums):
                return 1 if cs==target else 0
            
            if (cs,i) not in memo:
                memo[(cs,i)]=dp(cs-nums[i],i+1) +dp((cs+nums[i]),i+1)
            return memo[(cs,i)]
        
        return dp(0,0)
