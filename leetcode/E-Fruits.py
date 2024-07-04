import sys

n, m = map(int, sys.stdin.readline().split())
a = sorted(map(int, sys.stdin.readline().split()))
dic = {}
for _ in range(m):
    s = sys.stdin.readline().rstrip()
    dic[s] = dic.get(s, 0) + 1
dic = sorted(dic.values(), reverse=True)
res1 = sum(a[i] * dic[i] for i in range(len(dic)))
res2 = sum(a[-i-1] * dic[i] for i in range(len(dic)))
print(res1, res2)