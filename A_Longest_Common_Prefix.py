t= int(input())

phones = []
for _ in range(t):
    phones.append(input())

ans= phones[0]
for i in range(1, t):
    for j in range(len(ans)):
        if ans[j] != phones[i][j]:
            ans= ans[:j]
            break
print(len(ans))