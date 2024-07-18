from collections import defaultdict
t=int(input())
for _ in range(t):
    n, m = map(int, input().split(" "))
    inputs=[]
    for i in range(n):
        row = list(map(int, input().split()))
        inputs.append(row)
    
    
    
    dic_right=defaultdict(int)
    dic_left=defaultdict(int)
    for i in range(n):
        for j in range(m):
            dic_right[i-j]+=inputs[i][j]
            dic_left[i+j]+=inputs[i][j]
    ans=0
    for i in range(n):
        for j in range(m):
            ans=max(ans,(dic_right[i-j]+dic_left[i+j]-inputs[i][j]))
    print(ans)