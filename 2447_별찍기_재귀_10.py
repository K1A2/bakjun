def print_star():
    l = ['', '', '']
    for i in range(3):
        l[i] += print_star()
i = int(input())
print(print_star())