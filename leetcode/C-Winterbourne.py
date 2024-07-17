t = int(input())

for _ in range(t):
    total_sum = 0
    people, chair = list(map(int, input().split(" ")))

    rules = list(map(int, input().split(" ")))
    rules.sort(reverse=True)

    total_sum += people
    total_sum += rules[0]
    total_sum -= rules[-1]

    for rule in rules:
        total_sum += rule
    print('YES' if chair >= total_sum else 'NO')

