t=int(input())
for _ in range(t):
    n=int(input())
    inputs=list(map(int,input().split(" ")))
    trial_1=max(inputs)
    trial_2=min(inputs)
    if inputs.count(trial_1)==1:
        print(inputs.index(trial_1) +1)
    else:
        print(inputs.index(trial_2)+1)
    
