

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        memo = defaultdict(list)

        def dp(i):
            if i >= len(s):
                res.append(part.copy())
                return 

            

            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    part.append(s[i:j+1])
                    dp(j+1)
                    part.pop()


        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True

        dp(0)
        return res
