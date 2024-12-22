def find_meeting_time(x, y, a, b):
    distance = y - x
    h= a + b
    if distance % h == 0:
        return distance // h
    else:
        return -1

t = int(input())
for _ in range(t):
    data = list(map(int, input().split()))
    x, y, a, b = data[0], data[1], data[2], data[3]
    result = find_meeting_time(x, y, a, b)
    print(result)