n = int(input())
arr = list(map(int, input().split()))

odd_nums = []
even_nums = []

for num in arr:
    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num)

# If both odd and even numbers are present, sort the array
if odd_nums and even_nums:
    arr.sort()

print(" ".join(map(str, arr)))
