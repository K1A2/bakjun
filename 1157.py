s = input().lower()
d = dict()
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
m = ''
l = 0
for k, v in d.items():
    if l < v:
        m = k
        l = v
count = 0
for v in d.values():
    if v == l:
        count += 1
        if count > 1:
            print("?")
            exit(0)
print(m.upper())