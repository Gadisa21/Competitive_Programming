class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        
        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        
        for char in t:
            
            if char not in char_freq or char_freq[char] == 0:
                return False
            
            char_freq[char] -= 1
        
        
        return True
