def main():
    t = int(input())
    for _ in range(t):
        n, k, q = map(int, input().split())
        t = list(map(int, input().split()))
        pd = 0
        ans = 0
        for i in range(n):
            if t[i] <= q:
                pd += 1
            else:
                pd = 0
            ans += max(0, pd - k + 1)
        print(ans)

if __name__ == "__main__":
    main()
