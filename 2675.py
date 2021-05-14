for _ in range(int(input())):
    k, s = input().split()
    ns = ''
    for i in s:
        # for _ in range(k - 1):
        #     i += i
        ns += i * int(k)
print(ns)