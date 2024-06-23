from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        count = 0
        curr_len = 0
        
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                curr_len += 1
                count += curr_len
            else:
                curr_len = 0
        
        return count
