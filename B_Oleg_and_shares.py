def min_e(n, k, prices):
    min_price = min(prices)
    
    total_seconds = 0
    for price in prices:
        diff = price - min_price
        if diff % k != 0:
            return -1  
        total_seconds += diff // k
    
    return total_seconds



n ,k=list(map(int, input().split()))   
prices = list(map(int, input().split()))

result = min_e(n, k, prices)
print(result)
