def solve():
    arr = [input() for _ in range(8)]
    ans = ''.join([arr[i][j] for i in range(8) for j in range(8) if arr[i][j] != '.'])
    print(ans)

def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()
