n = int(input())
for i in range(1, n + 1):
    answer = i
    for m in str(i):
        answer += int(m)
    if answer == n:
        print(i)
        exit(0)
print(0)