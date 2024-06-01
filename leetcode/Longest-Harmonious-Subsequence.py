class Solution:
    def findLHS(self, nums: List[int]) -> int:

        hash_m=defaultdict(int)

        for num in nums:
            hash_m[num]+=1
        nums.sort()
        
        ans=0

        
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                ans=max(ans,hash_m[nums[i]]+hash_m[nums[i-1]])
        return ans