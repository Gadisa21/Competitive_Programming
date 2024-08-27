t=int(input())
for _ in range(t):
    inputs=int(input())
    if inputs>=1900:
        print("Division 1")
    elif inputs<=1899 and 1600<=inputs:
        print("Division 2")
    elif 1400<=inputs and inputs<=1599:
        print("Division 3")
    else:
        print("Division 4")
