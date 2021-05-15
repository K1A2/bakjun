l = []
for _ in range(int(input())):
    num = int(input())
    idx = 0
    for i in l:
        if i > num:
            break
        idx += 1
    l.insert(idx, num)
for i in l:
    print(i)