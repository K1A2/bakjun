k = int(input())
s = k - 1
for i in range(k):
    for _ in range(s):
        print(" ", end="")
    for _ in range(k - s):
        print("*", end="")
    print()
    s -= 1