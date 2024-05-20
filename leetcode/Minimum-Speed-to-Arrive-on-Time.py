from math import ceil
from typing import List

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        
        if hour < n - 1:
            return -1
        
        left, right = 1, 10**7
        answer = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            total_time = 0
            for i in range(n - 1):
                total_time += ceil(dist[i] / mid)
            total_time += dist[-1] / mid
            
            if total_time <= hour:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return answer
