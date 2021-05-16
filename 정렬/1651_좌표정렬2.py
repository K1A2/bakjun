import sys
def merge(l1, l2):
    merged_list = []
    while l1 != [] and l2 != []:
        t1, t2 = l1[0], l2[0]
        x1, x2, y1, y2 = t1[0], t2[0], t1[1], t2[1]
        if y1 > y2:
            merged_list.append(t2)
            l2 = l2[1:]
        elif y1 == y2:
            if x1 > x2:
                merged_list.append(t2)
                l2 = l2[1:]
            else:
                merged_list.append(t1)
                l1 = l1[1:]
        else:
            merged_list.append(t1)
            l1 = l1[1:]
    if l1 != []:
        merged_list += l1
    if l2 != []:
        merged_list += l2
    return merged_list

def merge_sort(l):
    if len(l) <= 1:
        return l
    n = len(l) // 2
    firat = merge_sort(l[:n])
    last = merge_sort(l[n:])
    return merge(firat, last)

n = int(sys.stdin.readline())
xy = [0 for _ in range(n)]
for i in range(n):
    xy[i] = tuple(map(int, sys.stdin.readline().split()))
s = ''
for i in merge_sort(xy):
    s += str(i[0]) + ' ' + str(i[1]) + '\n'
print(s)