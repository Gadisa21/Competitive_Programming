class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)  
        n = len(num_str)
        count = 0
        
        for i in range(n - k + 1):
            substring = num_str[i:i+k] 
            substring_int = int(substring) 
            
            if substring_int != 0 and num % substring_int == 0:
                count += 1
        
        return count
