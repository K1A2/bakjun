def print_star(num):
    if num == 3:
        return ['***', '* *', '***']
    else:
        la = ['' for _ in range(num)]
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    for m in range(num // 3):
                        la[m + num // 3] += ' ' * (num // 3)
                else:
                    n = print_star(num // 3)
                    for m in range(len(n)):
                        la[m + i * (num // 3)] += n[m]
        return la

answer = print_star(int(input()))
for i in answer:
    print(i)