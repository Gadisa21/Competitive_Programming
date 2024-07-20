def check_palindrome_subsequence(arr):
    n = len(arr)
    for i in range(n - 2):
        for j in range(i + 2, n):
            if arr[i] == arr[j]:
                return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(check_palindrome_subsequence(arr))
