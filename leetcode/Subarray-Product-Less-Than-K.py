class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l,r=0,0
        ans=0
        product=1
        while r<len(nums):
            product*=nums[r]
            while l<r and product>=k:
                product/=nums[l]
                l+=1
            if product<k:
                ans+=(r-l)+1 
            r+=1
        return ans

        