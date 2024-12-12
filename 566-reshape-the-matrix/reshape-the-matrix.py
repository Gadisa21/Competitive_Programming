class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        que=deque()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                que.append(mat[i][j])

        ans=[]
        
        for i in range(r):
            temp=[]
            for j in range(c):
                if not que:
                    return mat
                else:
                    temp.append(que.popleft())
            ans.append(temp)
        return ans if not que else mat

        