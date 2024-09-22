n=int(input())
res=0
for _ in range(n):
    nums=list(map(int,input().split(" ")))
    total=0
    
    for i in range(3):
        if nums[i]==1:
            total+=1
    if total>=2:
        res+=1
print(res)
    