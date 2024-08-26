def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ar = list(map(int, input().split()))
        for j in range(n // 2):
            print(ar[j], ar[n - j - 1], end=" ")
        if n % 2 != 0:
            print(ar[n // 2])
        else:
            print()

if __name__ == "__main__":
    main()
