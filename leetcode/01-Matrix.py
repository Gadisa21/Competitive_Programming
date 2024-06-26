from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return mat
        
        m, n = len(mat), len(mat[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        queue = deque()
        visited = set()
        
        result = [[-1 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))  
                    visited.add((i, j))
                    result[i][j] = 0
        
        def  inbound(row,col):
            return (0<=row<len(mat)) and (0<=col<len(mat[0]))
        
        while queue:
            row, col, distance = queue.popleft()
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if inbound(new_row,new_col) and (new_row, new_col) not in visited:
                    queue.append((new_row, new_col, distance + 1))
                    visited.add((new_row, new_col))
                    result[new_row][new_col] = distance + 1
        
        return result
