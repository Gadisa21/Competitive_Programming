t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    c = 0
    j = n - 1
    for i in range(n // 2):
        if s[i] == s[j - i]:
            break
        if s[i] != s[j - i]:
            c += 2
    print(n - c)
