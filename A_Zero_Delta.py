t=int(input())


for _ in range(t):
    n,k=list(map(int,input().split()))
    nums=list(map(int,input().split()))
    l,r=0,len(nums)-1
    while 0<k and l!=r:
        if nums[l]>0:
            nums[l]-=1
            nums[r]+=1
            k-=1
        else:
            l+=1
    print(*nums)
