
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()  
        
        left, right = 1, price[-1] - price[0]
        def can_select_with_min_diff(min_diff):
            count = 1  
            last_selected = price[0]
            
            for i in range(1, len(price)):
                if price[i] - last_selected >= min_diff:
                    count += 1
                    last_selected = price[i]
                    if count == k:
                        return True
            return False
        
        while left <= right:
            mid = (left + right) // 2
            if can_select_with_min_diff(mid):
                left = mid + 1  
            else:
                right = mid - 1  
            
        return right
