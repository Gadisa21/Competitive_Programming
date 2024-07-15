t=int(input())
for _ in range(t):
    word=input()
    n=len(word)
    if n>10:
        num=n-2
        print(f"{word[0]}{num}{word[-1]}")
    else:
        print(word)
