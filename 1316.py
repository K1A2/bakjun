count = 0
for _ in range(int(input())):
    a = set()
    s = input()
    last = s[0]
    a.add(s[0])
    s = s[1:]
    isR = True
    while s != '':
        if s[0] != last:
            if s[0] in a:
                isR = False
                break
        last = s[0]
        a.add(s[0])
        s = s[1:]
    if isR:
        count += 1
print(count)