class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count_freq=defaultdict(int)

        for s in words:
            count_freq[s]+=1
        
        count_val=defaultdict(list)

        for key,value in count_freq.items():
            count_val[value].append(key)
        
        for key, value in count_val.items():
            heapq.heapify(value)
        
        maxHeap=[-value for key,value in count_freq.items()]
        heapq.heapify(maxHeap)
        ans=[]
        
        while k>0:
            next_top=-heapq.heappop(maxHeap)
            ans.append(heapq.heappop(count_val[next_top]))
            k-=1
        
        return ans
        