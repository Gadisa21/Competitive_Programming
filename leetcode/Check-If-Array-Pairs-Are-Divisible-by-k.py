class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dic=defaultdict(int)

        for num in arr:
            dic[num%k]+=1
        if dic[0]%2!=0:
            return False
        for i in range(1,k):
            if dic[i]!=dic[k-i]:
                return False
        return True
