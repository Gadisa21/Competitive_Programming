class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        current_bits = 0
        max_length = 0

        for right in range(len(nums)):
            while (current_bits & nums[right]) != 0:
                current_bits ^= nums[left]
                left += 1
            
            current_bits |= nums[right]
            max_length = max(max_length, right - left + 1)
        
        return max_length