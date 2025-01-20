password = input().strip()
n = int(input().strip())
words = [input().strip() for _ in range(n)]

first_letter_matches = any(word[1] == password[0] for word in words)
second_letter_matches = any(word[0] == password[1] for word in words)
password_exact_match = password in words

if password_exact_match or (first_letter_matches and second_letter_matches):
    print("YES")
else:
    print("NO")
