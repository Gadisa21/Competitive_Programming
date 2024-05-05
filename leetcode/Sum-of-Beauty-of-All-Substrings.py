class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0
        
        for i in range(len(s)):
            freq = [0] * 26
            
            for j in range(i, len(s)):
                freq[ord(s[j]) - ord('a')] += 1
                
                max_freq = max(freq)
                min_freq = min(f for f in freq if f > 0)
                
                total_beauty += (max_freq - min_freq)
        
        return total_beauty
