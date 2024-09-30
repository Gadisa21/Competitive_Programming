n=int(input())
nums=list(map(int,input().split(" ")))
if n==1:
    print(0)
else:
    total=sum(nums)
    highest=max(nums)
    print(highest*n-total)