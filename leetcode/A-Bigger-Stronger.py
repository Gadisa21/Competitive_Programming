t=int(input())
for _ in range(t):
    n=int(input())
    inputs=list(map(int,input().split(" ")))
    my_set=set(inputs)
    if n==len(my_set):
        print("YES")
    else:
        print("NO")