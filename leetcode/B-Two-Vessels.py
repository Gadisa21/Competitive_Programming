def solve():
    a, b, c = map(int, input().split())
    mn = min(a, b)
    mx = max(a, b)
    ct = 0
    while mn < mx:
        mn += c
        mx -= c
        ct += 1
    print(ct)

def main():
    TC = int(input())
    for _ in range(TC):
        solve()

if __name__ == "__main__":
    main()
