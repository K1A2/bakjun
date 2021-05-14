count = 0
for i in range(1, int(input()) + 1):
    i = str(i)
    if len(i) <= 2:
        count += 1
    else:
        d = int(i[0]) - int(i[1])
        isR = True
        for k in range(1, len(i) - 1):
            if d != (int(i[k]) - int(i[k + 1])):
                isR = False
                break
        if isR:
            count += 1
print(count)