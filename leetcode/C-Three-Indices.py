def solve():
    n = int(input())
    p = list(map(int, input().split()))

    for i in range(1, n - 1):
        if p[i] > p[i - 1] and p[i] > p[i + 1]:
            print("YES")
            print(i, i + 1, i + 2)
            return
    
    print("NO")

def main():
    tests = int(input())
    while tests:
        solve()
        tests -= 1

if __name__ == "__main__":
    main()
