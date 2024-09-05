# Solution Start Here
def solve():
    n = int(input())
    v = list(map(int, input().split()))
    ans = list(range(1, n + 1))
    
    if n == 1:
        print(-1)
        return
    
    for i in range(n):
        if v[i] == ans[i]:
            if i + 1 <= n - 1:
                ans[i], ans[i + 1] = ans[i + 1], ans[i]
            else:
                ans[i], ans[i - 1] = ans[i - 1], ans[i]
    
    print(*ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
