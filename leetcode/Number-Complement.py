class Solution:
    def findComplement(self, num: int) -> int:
        num_bits = num.bit_length()
        
        m = (1 << num_bits) - 1
        
        complement = num ^ m
        
        return complement
