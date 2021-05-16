import sys
n = int(sys.stdin.readline())
people = []
for _ in range(n):
    person = sys.stdin.readline().strip().split()
    people.append((int(person[0]), person[1]))
people.sort(key=lambda p: p[0])
for i in people:
    print(str(i[0]) + ' ' + i[1])