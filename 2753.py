i = int(input())
if i % 400 == 0 and i % 4 == 0:
    print(1)
else:
    if i % 4 == 0 and not i & 100 == 0:
        print(1)
    else:
        print(0)