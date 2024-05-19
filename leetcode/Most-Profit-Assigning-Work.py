class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        pairs=list(zip(profit,difficulty))

        pairs.sort()
        worker.sort()
        index=len(pairs)-1
        print(pairs)

        total_profit=0
        for i in range(len(worker)-1,-1,-1):
            if pairs[index][1]<=worker[i]:
                total_profit+=pairs[index][0]
            else:
                while index>=0 and pairs[index][1]>worker[i]:
                    index-=1
                if index<0:
                    return total_profit
                else:
                    total_profit+=pairs[index][0]
        return total_profit

        

        
        