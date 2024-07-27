q = int(input())

for _ in range(q):
    n, k = map(int, input().split())
    prices = list(map(int, input().split()))

    min_price = min(prices)
    max_price = max(prices)

    if max_price - min_price > 2 * k:
        print(-1)
    else:
        B = min_price + k
        print(B)