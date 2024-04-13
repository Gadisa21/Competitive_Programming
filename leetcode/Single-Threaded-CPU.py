class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        if len(tasks)==1:
            return [0]


        for i,task in enumerate(tasks):
            task.append(i)
        tasks.sort()
        minHeap=[]
        i=0
        t=tasks[i][0]
        while i<len(tasks) and t>=tasks[i][0]:
            heapq.heappush(minHeap,(tasks[i][1],tasks[i][-1]))
            i+=1
        ans=[]
        
        while minHeap:
            tim,index=heapq.heappop(minHeap)
            t+=tim
            ans.append(index)
            
            while i<len(tasks) and t>=tasks[i][0]:
                heapq.heappush(minHeap,(tasks[i][1],tasks[i][-1]))
                i+=1
            if len(minHeap)==0:
                if i <len(tasks):
                    t=tasks[i][0]
                    while i<len(tasks) and t>=tasks[i][0]:
                        heapq.heappush(minHeap,(tasks[i][1],tasks[i][-1]))
                        i+=1
        return ans


        