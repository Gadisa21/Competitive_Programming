import math

def main():
    n = int(input())
    if n == 3:
        print(1, 2)
        return
    
    a = (n // 2) - 1
    b = (n // 2) + 1
    if n % 2 == 1:
        a += 1
    
    div = math.gcd(a, b)
    if div != 1:
        a -= 1
        b += 1
    
    print(a, b)

if __name__ == "__main__":
    main()
