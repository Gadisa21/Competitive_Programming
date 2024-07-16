for _ in range(int(input())):
    n, x1, y1, x2, y2= map(int, input().split())
    m= n//2

    if x1>m:
        x1= n+1-x1
    if x2>m:
        x2= n+1-x2
    if y1>m:
        y1= n+1-y1
    if y2>m:
        y2= n+1-y2

    print(abs(min(x1, y1)-min(x2, y2)))