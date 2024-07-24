n, k = map(int, input().split()) 
a = list(map(int, input().split())) 
a.sort() 
 
if k == 0: 
    num = a[0] - 1 
else: 
    num = a[k-1] 
 
count = 0 
for i in range(n): 
    if a[i] > num: 
        break 
    else: 
        count += 1 
 
if num < 1 or count != k: 
    print(-1) 
else: 
    print(num)