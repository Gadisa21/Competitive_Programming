class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = Counter(s)
        
        sorted_chars = sorted(char_count.items(), key=lambda x: -x[1])
        
        if sorted_chars[0][1] > (len(s) + 1) // 2:
            return ""
        
        res = [''] * len(s)
        index = 0
        
        for char, freq in sorted_chars:
            for _ in range(freq):
                res[index] = char
                index += 2
                if index >= len(s):
                    index = 1
        
        return ''.join(res)
