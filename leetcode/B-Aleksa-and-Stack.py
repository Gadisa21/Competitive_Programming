# Read the number of test cases
t = int(input())

tcase = 0

# Iterate through each test case
while t > 0:
    tcase += 1
    t -= 1
    
    # Read the value of n
    n = int(input())
    
    f = 1
    l = 3
    
    # Generate and output the array
    for i in range(n):
        if (l + 1) % 3 == 0:
            l += 1
        print(l, end=' ')
        l += 1
    
    print()
