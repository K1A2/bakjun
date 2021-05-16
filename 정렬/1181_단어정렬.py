import sys
n = int(sys.stdin.readline())
words = dict()
for i in range(50):
    words[i] = []
for _ in range(n):
    s = sys.stdin.readline().strip()
    c = len(s) - 1
    l = words[c]
    if s not in l:
        l.append(s)
        words[c] = l
for v in words.values():
    v.sort()
    for i in v:
        print(i)