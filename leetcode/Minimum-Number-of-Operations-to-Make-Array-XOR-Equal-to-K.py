class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor_arr=0

        for num in nums:
            xor_arr ^=num
        operation=0
        
        for i in range(33):
            if (xor_arr >> i) & 1 != (k >> i) & 1:
                operation += 1
        return operation 