class Solution(object):
    def twoSum(self, nums, target):
        num_to_index = {}  # Dictionary to store numbers and their indices

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

        # If no solution found, return an empty list
        return []
