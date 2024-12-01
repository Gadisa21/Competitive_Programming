t=int(input())

for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))

    cur_pa=(nums[0]%2==0)
    if n==1:
        print(0)
    else:
        op=0
        count=1
        for i in range(1,n):
            if cur_pa==(nums[i]%2==0):
                count+=1
            else:
                cur_pa=(nums[i]%2==0)
                op+=(count-1)
                count=1
        op+=(count-1)
        print(op)
