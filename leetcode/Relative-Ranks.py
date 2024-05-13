class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        index_map={num:i for i,num in enumerate(score)}
        rank={}

        score.sort(reverse=True)
        for i in range(len(score)):
            if i<3:
                if i==0:
                    rank[score[i]]="Gold Medal"
                elif i==1:
                    rank[score[i]]="Silver Medal"
                else:
                    rank[score[i]]="Bronze Medal"
            else:
                rank[score[i]]=str(i+1)
        ans=[0]*len(score)
        for key,value in index_map.items():
            ans[value]=rank[key]
        return ans


        