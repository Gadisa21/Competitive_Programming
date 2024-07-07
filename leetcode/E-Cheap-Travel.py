def main():
    n, m, a, b = map(int, input().split())

    if m * a > b:
        remain = (n % m) * a
        if remain > b:
            print(n // m * b + b)
        else:
            print(n // m * b + remain)
    else:
        print(n * a)

if __name__ == "__main__":
    main()
