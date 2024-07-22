test = int(input())

for _ in range(test):

    n = int(input())
    arr = list(map(int, input().split()))
 
    if n & 1:
        print(4)
        print(*[1,n-1])
        print(*[1,n-1])
        print(*[n-1,n])
        print(*[n-1, n])

    else:
        print(2)
        print(*[1,n])
        print(*[1, n])