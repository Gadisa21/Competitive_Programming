t= int(input())
for _ in range(t):
    valid=""
    input1=input()
    if len(input1)==2:
        print(input1)
    else:
        for i in range(1,len(input1)-2,2):
            valid+=input1[i]
        valid=input1[0]+valid+input1[-1]
        print(valid)
