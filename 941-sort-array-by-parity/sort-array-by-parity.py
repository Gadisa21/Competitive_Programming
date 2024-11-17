class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens = [num for num in nums if num % 2 == 0]
        odds = [num for num in nums if num % 2 != 0]
        return evens + odds