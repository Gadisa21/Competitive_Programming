M = 10**9 + 7

def mod(x):
    return (x % M + M) % M

def mul(a, b):
    return mod(a * b)

def add(a, b):
    return mod(a + b)

def solve():
    n = int(input())
    s = input()
    a = [0] * 26
    a[ord(s[0]) - ord('A')] = 1
    for i in range(1, n):
        if s[i] == s[i - 1]:
            continue
        else:
            if a[ord(s[i]) - ord('A')] > 0:
                print("NO")
                return
            a[ord(s[i]) - ord('A')] = 1
    print("YES")

t = int(input())
for _ in range(t):
    solve()