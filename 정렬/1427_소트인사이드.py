s = list(map(int, input()))
s.sort()
s.reverse()
print(''.join(map(str, s)))