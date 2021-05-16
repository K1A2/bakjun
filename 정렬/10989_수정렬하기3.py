import sys
n = int(sys.stdin.readline())
count = [0 for _ in range(10001)]
for i in range(n):
    count[int(sys.stdin.readline())] += 1
for i in range(10001):
    for _ in range(count[i]):
        sys.stdout.write(str(i) + '\n')