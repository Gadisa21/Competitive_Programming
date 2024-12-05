class SeatManager:

    def __init__(self, n: int):
        self.minHeap=[]
        for i in range(1,n+1):
            heapq.heappush(self.minHeap,i)
        

    def reserve(self) -> int:
        return heapq.heappop(self.minHeap)
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.minHeap,seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)