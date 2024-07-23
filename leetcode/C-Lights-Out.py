def main():
    grid = [list(map(int, input().split())) for _ in range(3)]
    for i in range(3):
        for j in range(3):
            switch_count = grid[i][j]
            if i > 0:
                switch_count += grid[i - 1][j]
            if i < 2:
                switch_count += grid[i + 1][j]
            if j > 0:
                switch_count += grid[i][j - 1]
            if j < 2:
                switch_count += grid[i][j + 1]
            
            print(1 if switch_count % 2 == 0 else 0, end='')
        print()

if __name__ == "__main__":
    main()
