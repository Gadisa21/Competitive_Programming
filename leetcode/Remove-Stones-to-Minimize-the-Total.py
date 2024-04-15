class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles=[ -stone for stone in piles]

        heapify(piles)

        while k!=0:
            num=heappop(piles)
            num//=2
            heappush(piles,num)
            k-=1
        return -sum(piles)


        