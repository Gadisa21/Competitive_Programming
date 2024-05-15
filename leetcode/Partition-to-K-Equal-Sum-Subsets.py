class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k:
            return False
        nums.sort(reverse=True)
        
        target=sum(nums)//k
        if nums[0] > target:
            return False
        used=[False]*len(nums)

        def back(i,k,subsum):
            if k==1:
                return True
            if subsum==target:
                return back(0,k-1,0)
            for  j in range(i,len(nums)):
                if used[j] or subsum + nums[j]>target:
                    continue
                used[j]=True
                if back(j+1,k,subsum+nums[j]):
                    return True
                used[j]=False
            return False
        return back(0,k,0)

        