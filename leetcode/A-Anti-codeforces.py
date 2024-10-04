t=int(input())
for _ in range(t):
    codeforce="codeforces"
    input1=input()
    ans=0
    for i in range(len(input1)):
        if input1[i]!=codeforce[i]:
            ans+=1
    print(ans)
