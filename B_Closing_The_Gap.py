t=int(input())

for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    total_sum=sum(nums)

    if total_sum%n!=0:
        print(1)
    else:
        print(0)