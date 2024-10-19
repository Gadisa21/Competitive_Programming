class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        
        for i in range(len(s) - 2):
            substring = s[i:i+3]  
            
            if len(set(substring)) == 3:
                count += 1
        
        return count
