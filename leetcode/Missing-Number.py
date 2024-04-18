class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        missing_num=len(nums)
        i=0

        while i<len(nums):
            if nums[i]==len(nums):
                missing_num=i
                i+=1
            else:
                if nums[i]!=i:
                    j=nums[i]
                    if nums[j]==len(nums):
                        missing_num=i
                    nums[i],nums[j]=nums[j],nums[i]
                else:
                    i+=1
        return missing_num
        