def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    if arr[0] != n:
        print("No")
        return

    freq = [0] * (n + 1)
    for i in range(n):
        freq[arr[i]] += 1

    for i in range(n - 1, 0, -1):
        freq[i] += freq[i + 1]

    for i in range(1, n + 1):
        if arr[i - 1] != freq[i]:
            print("No")
            return

    print("Yes")


T = int(input())
for _ in range(T):
    solve()
