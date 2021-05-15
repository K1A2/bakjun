n = int(input())
count = 0
num = 665
while True:
    s = str(num)
    for i in range(len(s) , 2, -1):
        if s[i - 3:i] == '666':
            count += 1
            break
    if count == n:
        print(num)
        break
    num += 1