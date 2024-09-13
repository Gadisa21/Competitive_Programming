t = int(input())
dic = {}
for _ in range(t):
    name = input()
    if name in dic:
        dic[name] += 1
        new_name = name + str(dic[name])
        print(new_name)
        dic[new_name] = 0
    else:
        print("OK")
        dic[name] = 0
