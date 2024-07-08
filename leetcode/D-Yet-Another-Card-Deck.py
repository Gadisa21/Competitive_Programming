def solve():
    n, q = map(int, input().split())
    colors = list(map(int, input().split()))
    color_positions = [float('inf')] * 51

    for i, color in enumerate(colors):
        color_positions[color] = min(color_positions[color], i + 1)

    queries = list(map(int, input().split()))

    for query in queries:
        position = color_positions[query]
        print(position, end=" ")

        # Update color_positions and shift other colors up
        color_positions[query] = 1
        for j in range(1, 51):
            if j == query:
                continue
            if color_positions[j] < position:
                color_positions[j] += 1
    print()

if __name__ == "__main__":
    testcases = 1
    for _ in range(testcases):
        solve()
