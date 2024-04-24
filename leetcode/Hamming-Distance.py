class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_r = x ^ y  
        hamming_dist = 0
        while xor_r:
            hamming_dist += xor_r & 1
            xor_r >>= 1
        return hamming_dist
