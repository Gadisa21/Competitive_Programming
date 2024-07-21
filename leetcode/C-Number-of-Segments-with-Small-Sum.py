n,s=list(map(int,input().split()))
nums=list(map(int,input().split()))
l=0
count=0
current_sum=0

for r in range(n):
    current_sum+=nums[r]
    if current_sum>s:
        while current_sum>s:
            current_sum-=nums[l]
            l+=1
    count+=(r-l+1)
print(count)
        
