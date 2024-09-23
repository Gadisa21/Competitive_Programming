def solve():
    n = int(input())
    intervals = [tuple(map(int, input().split())) for _ in range(n)]
    for i in range(1, n):
        if intervals[i][0] >= intervals[0][0] and intervals[i][1] >= intervals[0][1]:
            print(-1)
            return
    print(intervals[0][0])

TC = int(input())
for _ in range(TC):
    solve()
