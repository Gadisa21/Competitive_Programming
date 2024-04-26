class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates=set()
        i=0
        while i<len(nums):
            if i==nums[i]-1:
                i+=1
            else:
                j=nums[i]-1
                if nums[j]==nums[i]:
                    duplicates.add(nums[i])
                    i+=1
                else:
                    nums[i],nums[j]=nums[j],nums[i]
        return list(duplicates)


        