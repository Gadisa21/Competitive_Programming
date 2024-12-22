t = int(input())

for _ in range(t):
    n = int(input())
    
    s = input()
    
    zero_count = s.count('0')
    
    if zero_count % 2 == 1 and zero_count > 1:
        print("ALICE")
    else:
        print("BOB")