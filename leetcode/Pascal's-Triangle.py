class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        
        if numRows==1:
            return ans
        
        for i in range(2,numRows+1):
            sum_num=ans[-1][0]
            temp=[ans[-1][0]]
            for j in range(1,len(ans[-1])):
                sum_num+=ans[-1][j]
                temp.append(sum_num)
                sum_num=ans[-1][j]
            temp.append(1)
            ans.append(temp)
        return ans
                
