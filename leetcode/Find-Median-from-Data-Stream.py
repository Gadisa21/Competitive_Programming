class MedianFinder:

    def __init__(self):
        self.minHeap=[]
        self.maxHeap=[]
        self.n=0
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap,-num)

        if len(self.minHeap)!=0 and len(self.maxHeap)!=0 and -self.minHeap[0]>self.maxHeap[0]:
            heapq.heappush(self.maxHeap,-heapq.heappop(self.minHeap))
      
        if len(self.maxHeap)>len(self.minHeap)+1:
            heapq.heappush(self.minHeap,-heapq.heappop(self.maxHeap))
        if len(self.maxHeap)+1<len(self.minHeap):
            heapq.heappush(self.maxHeap,-heapq.heappop(self.minHeap))
        
        self.n+=1

    def findMedian(self) -> float:
        if self.n%2!=0:
            if len(self.maxHeap)>len(self.minHeap):
                return self.maxHeap[0]
            else:
                return -self.minHeap[0]
        else:
            return (-self.minHeap[0]+self.maxHeap[0])/2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()