t=int(input())

for _ in range(t):
    s=input()
    num1=int(s[0])
    op=s[1]
    num2=int(s[2])

    if op=="<":
        if num1<num2:
            print(s)
        elif num1==num2:
            print(num1,num2,sep="=")
        else:
            print(num1,num2,sep=">")
    elif op==">":
        if num1>num2:
            print(s)
        elif num1==num2:
            print(num1,num2,sep="=")
        else:
            print(num1,num2,sep="<")
    else:
        if num1==num2:
            print(s)
        else:
            if num1<num2:
                print(num1,num2,sep="<")
            else:
                print(num1,num2,sep=">")
