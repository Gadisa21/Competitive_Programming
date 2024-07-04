t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Length of the string
    s = input()  # Input string
    diffs = [0] * n
    sum = 0

    for p in range(n):
        cur = p if s[p] == 'L' else n - p - 1
        mx = p if p > n - p - 1 else n - p - 1
        sum += cur
        diff = mx - cur
        diffs[p] = diff

    diffs.sort(reverse=True)

    for p in range(n):
        sum += diffs[p]
        print(sum, end=" ")
    print()
