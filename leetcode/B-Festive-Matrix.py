n=int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
ans=0
i=0
while i<n:
    ans+=matrix[i][i]
    i+=1
i=0
j=n-1
while j!=0:
    ans+=matrix[i][j]
    i+=1
    j-=1
ans += matrix[i][j]
i=(n-1)//2
j=0
while j!=n:
    ans+=matrix[i][j]
    j+=1
j = (n-1)//2
i=0
while i!=n:
    ans+=matrix[i][j]
    i+=1
ans=ans-3*(matrix[j][j])
print(ans)
