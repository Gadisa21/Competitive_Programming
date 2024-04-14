class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix[0])-1
        row=0

        while row<len(matrix) and l<=r :
            mid=l+(r-l)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]<target:
                l=mid+1
            elif matrix[row][mid]>target:
                r=mid-1
            
        
            if l>r:
                row+=1
                l=0
                r=len(matrix[0])-1
                
        return False
                
        