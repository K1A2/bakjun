d = [dict(), dict()]
for _ in range(3):
    x = list(map(int, input().split()))
    for i in range(len(x)):
        if x[i] in d[i]:
            d[i][x[i]] += 1
        else:
            d[i][x[i]] = 1
a = []
for dd in d:
    for k, v in dd.items():
        if v == 1:
            a.append(k)
            break
print(a[0], a[1])