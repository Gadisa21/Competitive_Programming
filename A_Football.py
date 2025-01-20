n = int(input())
a = int(input())
b = int(input())

draws = min(a, b)  # The minimum possible number of draws

print(draws)

# Distribute draws first
for i in range(draws):
    print("1:1")
    a -= 1
    b -= 1

# Distribute remaining matches with wins and losses
for i in range(n - draws):
    if a > 0:
        print(f"{a}:0")
        a -= a  # Exhaust all remaining goals scored
    else:
        print(f"0:{b}")
        b -= b  # Exhaust all remaining goals conceded
