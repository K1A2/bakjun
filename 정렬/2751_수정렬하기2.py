import sys
def merge_sort(l1, l2):
    lm = len(l1)
    lm2 = len(l2)
    an = []
    if lm > 1:
        l1 = merge_sort(l1[:lm // 2], l1[lm // 2:])
    if lm2 > 1:
        l2 = merge_sort(l2[:lm2 // 2], l2[lm2 // 2:])
    while l1 != [] or l2 != []:
        if l1 != [] and l2 != []:
            x1, x2 = l1[0], l2[0]
            if x1 > x2:
                an += [x2]
                l2 = l2[1:]
            else:
                an += [x1]
                l1 = l1[1:]
        elif l1 == []:
            an += l2
            break
        else:
            an += l1
            break
    return an
n = int(sys.stdin.readline())
l = [0] * n
for i in range(n):
    l[i] = int(sys.stdin.readline())
s = ''
for i in merge_sort(l[:n // 2], l[n // 2:]):
    s += str(i) + '\n'
sys.stdout.write(s)