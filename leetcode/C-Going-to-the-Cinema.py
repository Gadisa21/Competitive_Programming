t=int(input())
result=[]
for i in range(t):
    n=int(input())
    ai=list(map(int,input().split(" ")))
    res=0
    ai.sort()
    for j in range(n-1):
        if((ai[j+1]>j+1)&(j>=ai[j])):
            res+=1
    if(ai[-1]<=n-1):
        res+=1
    for j in range(n-1):
        peopleWent=n-j-1
        if((peopleWent<ai[j])&(peopleWent>=ai[-1])):
            res+=1
        else:
            break
    if((ai[0]!=0)&(ai[-1]!=0)):
        res+=1
    result.append(res)
for i in result:
    print(i)