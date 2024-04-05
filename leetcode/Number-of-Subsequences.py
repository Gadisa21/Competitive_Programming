class Solution(object):
    def numSubseq(self, nums, target):
        nums.sort()
        l,r=0,len(nums)-1
        mod=10**9 + 7
        res=0
        while l<=r:
            if nums[l]+nums[r]>target:
                r-=1
            else:
                res+=(2**(r-l))
                l+=1
        return res%mod

      
                



                

      
        