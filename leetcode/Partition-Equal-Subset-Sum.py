class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums)%2==1:
            return False
        memo=set()

        hs=sum(nums)/2

        def dp(i,cs):
            if cs ==hs:
                return True
            
            if cs>hs or i>=len(nums):
                return False

            if (i,cs) in memo:
                return False
            else:
                memo.add((i,cs))

            pick=dp(i+1,cs+nums[i])
            if  pick:
                return True
            not_pick=dp(i+1,cs)
            if not_pick:
                return True
            return False
        return dp(0,0)

                 
            
            

        
        