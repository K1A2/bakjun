import sys
n = int(sys.stdin.readline())
numbers = [0 for _ in range(n)]
count = dict()
for i in range(n):
    num = int(sys.stdin.readline())
    numbers[i] = num
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
numbers.sort()
print(int(round(sum(numbers) / n, 0)))
print(numbers[n // 2])
count_max = max(count.values())
a = []
for k, v in count.items():
    if v == count_max:
        a.append(k)
a.sort()
if len(a) == 1:
    print(a[0])
else:
    print(a[1])
print(max(numbers) - min(numbers))