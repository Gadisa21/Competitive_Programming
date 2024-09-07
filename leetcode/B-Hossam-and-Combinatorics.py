t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Number of elements in the array
    arr = list(map(int, input().split()))  # Elements of the array as a list
    
    mini = min(arr)  # Minimum element in the array
    maxi = max(arr)  # Maximum element in the array
    
    sc = arr.count(mini)  # Count of occurrences of the minimum element
    mc = arr.count(maxi)  # Count of occurrences of the maximum element
    
    if sc == n or mc == n:
        print(n * (n - 1))
    else:
        print(sc * mc * 2)
