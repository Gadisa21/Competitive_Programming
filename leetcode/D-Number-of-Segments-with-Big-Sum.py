n,s=list(map(int,input().split()))
nums=list(map(int,input().split()))

count=0
l=0
current_sum=0
for r in range(n):
    current_sum+=nums[r]
    while current_sum>=s:
        count+=(1+n-1-r)
        current_sum-=nums[l]
        l+=1
print(count)

