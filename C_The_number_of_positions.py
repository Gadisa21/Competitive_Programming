nums=list(map(int,input().split()))
n=nums[0]
a=nums[1]
b=nums[2]
ans=abs((a+1)-(n-b))+2
if a==0 and b==0:
    ans=n
print(ans)