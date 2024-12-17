class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        diff=sum(nums)-x
        if diff<0:
            return -1
        if diff==0:
            return len(nums)

        l=0
        count=0
        res=len(nums)
        prefix=0
        for i in range(len(nums)):
            prefix+=nums[i]
            count+=1
            while prefix>diff:
                count-=1
                prefix-=nums[l]
                l+=1
            if prefix==diff:
                res=min(res,(len(nums)-count))
                count-=1
                prefix-=nums[l]
                l+=1
        return res if res!=len(nums) else -1
