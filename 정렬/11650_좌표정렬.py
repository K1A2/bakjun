import sys
n = int(sys.stdin.readline())
xy = [0 for _ in range(n)]
for i in range(n):
    xy[i] = tuple(map(int, sys.stdin.readline().split()))
for i in range(n):
    for j in range(n):
        x1, y1 = xy[i][0], xy[i][1]
        x2, y2 = xy[j][0], xy[j][1]
        if x1 < x2:
            xy[i], xy[j] = xy[j], xy[i]
        elif x1 == x2:
            if y1 < y2:
                xy[i], xy[j] = xy[j], xy[i]
s = ''
for i in xy:
    s += str(i[0]) + " " + str(i[1]) + '\n'
sys.stdout.writelines(s)