class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        minHeap=[]
        mapC=[]

        for t in  range(len(profits)):
            mapC.append([capital[t],profits[t]])
        mapC.sort()
        j=0
        for i in range(k):
            while j<len(profits) and w>=mapC[j][0]:
                heapq.heappush(minHeap,-mapC[j][-1])
                j+=1
            if minHeap:
                p=-heapq.heappop(minHeap)
                
                w+=p
           
           
        return w
            
        