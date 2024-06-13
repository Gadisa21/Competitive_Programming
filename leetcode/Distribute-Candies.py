class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)
        candyType=set(candyType)
        if n//2>len(candyType):
            return len(candyType)
        else:
            return n//2

        