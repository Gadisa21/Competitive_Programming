n=int(input())
mylist=[]
for _ in range(n):
    inputs=input()
    mylist.append(inputs)
def comparator(element):
    return len(element)

check=True
mylist = sorted(mylist, key=lambda x: comparator(x))
for i in range(n-1):
    if mylist[i] not in mylist[i+1]:
        print("NO")
        check=False
        break
if check:
    print("YES")
    for i in  range(n):
        print(mylist[i])



