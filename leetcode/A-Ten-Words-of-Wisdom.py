def solve():
    n = int(input())

    currWinner = 0
    pos = 0

    for i in range(n):
        m, q = map(int, input().split())

        if m <= 10:
            if q > currWinner:
                currWinner = q
                pos = i + 1

    print(pos)

def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()
