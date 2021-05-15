l = []
def move(N, start, to, c):
    l.append(start + " " + to)

def hanoi(n, s, t, d, count):
    if n == 1:
        move(1, s, t, count)
        count += 1
    else:
        count = hanoi(n-1, s, d, t, count)
        move(n, s, t, count)
        count += 1
        count = hanoi(n-1, d, t, s, count)
    return count

print(hanoi(int(input()), '1', '3', '2', 0))
for i in l:
    print(i)