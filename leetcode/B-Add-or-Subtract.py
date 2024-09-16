t=int(input())
for _ in range(t):
    nums=list(map(int,input().split(" ")))
    a,b,c=nums
    if a+b==c:
        print("+")
    else:
        print("-")
