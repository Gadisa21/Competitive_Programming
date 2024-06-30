def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))

def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    if is_sorted(a):
        print("yes")
        print(1, 1)
        return
    
    sorted_a = sorted(a)
    
    start, end = 0, n - 1
    while a[start] == sorted_a[start]:
        start += 1
    while a[end] == sorted_a[end]:
        end -= 1
    segment = a[start:end+1]
    
    if is_sorted(segment[::-1]):
        print("yes")
        print(start + 1, end + 1)
    else:
        print("no")

if __name__ == "__main__":
    main()
