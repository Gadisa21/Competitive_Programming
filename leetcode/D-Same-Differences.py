def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        x_list = list(map(int, input().split()))
        mp = {}
        maxi = 0
        
        for i in range(n):
            x = x_list[i]
            if x - i in mp:
                maxi += mp[x - i]
            if x - i in mp:
                mp[x - i] += 1
            else:
                mp[x - i] = 1
        
        print(maxi)

if __name__ == "__main__":
    main()
