class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        dic={"a","e","i","o","u"}
        ans=0

        for i, char in enumerate(words):
            if (char[0] in dic and char[-1] in dic)  and (left<=i and i<=right):
                ans+=1
        return ans

        