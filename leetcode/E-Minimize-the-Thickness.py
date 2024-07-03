for i in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))

    y= []
    for j in range(1, n):
        summ= sum(a[:j])
        p= j-1
        z= p+1
        q= 0
        for k in range(j, n):
            q += a[k]
            if k == n-1 and q == summ:
                z= max(z, k-p)
                y.append(z)
            elif q == summ:
                v= k
                z= max(z, v-p)
                p= v
                q= 0
            elif q>summ:
                break

    if y == []:
        print(n)
    else:
        print(min(y))