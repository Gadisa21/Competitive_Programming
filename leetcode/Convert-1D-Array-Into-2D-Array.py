class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if m*n!=len(original):
            return []
        ans=[]
        j=0
        step=n
        for i in range(m):
            ans.append(original[j:n])
            j+=step
            n+=(step)
        return ans
        