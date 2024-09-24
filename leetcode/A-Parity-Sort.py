def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = sorted(a)
        f = 0
        for i in range(n):
            if (a[i] + b[i]) % 2 != 0:
                f = 1
                break
        print("NO" if f else "YES")

if __name__ == "__main__":
    main()
