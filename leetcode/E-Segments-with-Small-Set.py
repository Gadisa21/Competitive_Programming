n,s=list(map(int,input().split()))
nums=list(map(int,input().split()))

dic={}
l=0
count=0
for r in range(n):
    dic[nums[r]]=dic.get(nums[r],0)+1
    
    
    while len(dic)>s:
        dic[nums[l]]-=1
        if dic[nums[l]]==0:
            del dic[nums[l]]
        l+=1
    count += r-l+1
        

print(count)
