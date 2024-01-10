class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans=float("-inf")
        l,r=0,0
        average=0
        total=0
        while r<len(nums):
            total+=nums[r]
            if r-l+1==k:
                average=total/k
                ans=max(ans,average)
                total-=nums[l]
                l+=1
            r+=1
        return ans
       
        
       
        