t = int(input())

for _ in range(t):
    input1 = input()
    check = True

    if "ss" in input1 or "YY" in input1 or "ee" in input1:
        print("NO")
    else:
        if len(input1) == 1:
            if input1 in "Yes":
                print("YES")
            else:
                print("NO")
        else:
            for i in range(len(input1) - 1):
                if input1[i:i+2] not in ["Ye", "es","sY"]:
                    print("NO")
                    check = False
                    break  
            if check:
                print("YES")
