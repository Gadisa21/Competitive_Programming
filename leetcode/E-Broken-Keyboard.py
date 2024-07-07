def solve():
    s = input().strip()
    ans = set()
    cnt = 1

    for i in range(1, len(s) + 1):
        if i == len(s):
            if cnt % 2 != 0:
                ans.add(s[i - 1])
            break

        if s[i - 1] != s[i]:
            if cnt % 2 != 0:
                ans.add(s[i - 1])
            cnt = 0
        cnt += 1

    print("".join(sorted(ans)))

def main():
    n = int(input())
    for _ in range(n):
        solve()

if __name__ == "__main__":
    main()
