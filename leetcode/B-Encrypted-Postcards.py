t=int(input())
for _ in range(t):
    n=int(input())
    inputs=input()
    placeholder,seeker=0,1
    decripted=""
    while seeker<n:
        if inputs[placeholder]==inputs[seeker]:
            decripted+=inputs[placeholder]
            placeholder=seeker+1
            seeker+=1
        seeker+=1
    print(decripted)
        

