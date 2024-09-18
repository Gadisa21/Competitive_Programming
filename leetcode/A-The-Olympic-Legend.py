t=int(input())
for _ in range(t):
    distances=list(map(int,input().split()))
    kenenisa_distance=distances[0]
    number_of_athlets=0
    for i in range(len(distances)):
        if kenenisa_distance<distances[i]:
            number_of_athlets+=1
    print(number_of_athlets)
