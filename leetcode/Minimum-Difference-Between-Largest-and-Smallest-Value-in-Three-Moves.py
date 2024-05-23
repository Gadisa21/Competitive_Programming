class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4:
            return 0
        nums.sort()

        ans=float("inf")

        for i in range(4):
            j=len(nums)-4 + i
            ans=min(ans,nums[j]-nums[i])
        return ans
        
            

        

        