def find_equal_sum(n, ar):
    sum1 = 0
    sum2 = 0
    ans = 0
    l = 0
    r = n - 1
    while l <= r:
        if sum1 < sum2:
            sum1 += ar[l]
            l += 1
        else:
            sum2 += ar[r]
            r -= 1
        if sum1 == sum2:
            ans = sum1
    return ans

n = int(input())
ar = list(map(int, input().split()))
result = find_equal_sum(n, ar)
print(result)