import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))

number2 = sorted(list(set(number)))
dic = {number2[i] : i for i in range(len(number2))}
for i in number:
    print(dic[i], end = ' ')