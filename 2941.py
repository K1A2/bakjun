cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
str = input()
count = 0
while str != '':
    isC = False
    for i in cro:
        if str.startswith(i):
            count += 1
            isC = True
            str = str[len(i):]
            break
    if not isC:
        count += 1
        str = str[1:]
print(count)