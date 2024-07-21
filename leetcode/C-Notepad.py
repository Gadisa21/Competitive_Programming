t=int(input())
for _ in range(t):
    n=int(input())
    input1=input()
    check=True
    if n<=3:
        print("NO")
    else:
        for i in range(n-3):
            if input1[i:i+2] in input1[i+2:n]:
                print("YES")
                check=False
                break
        if check:
            print("NO")

